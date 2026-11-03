#!/usr/bin/env python3
"""
llm.py - a tiny client for any OpenAI-compatible chat API, with retries, a cost log and a spending cap.

WHY THIS EXISTS
  You will call a big "teacher" model (DeepSeek, or anything else with an OpenAI-style API) thousands of
  times: to extract questions from past papers, to write tutoring dialogues, to judge answers, to analyse
  failures. This file is the one place that talks to it, so you can change provider by editing .env.

SETUP  (copy .env.example to .env in the kit folder and fill it in)
  TEACHER_BASE_URL=https://api.deepseek.com          # any OpenAI-compatible base URL
  TEACHER_API_KEY=sk-...
  TEACHER_MODEL=deepseek-chat                         # check your provider's docs for the current model id
  TEACHER_PRICE_IN=0.15                               # US$ per million input tokens  (for the cost log)
  TEACHER_PRICE_OUT=0.60                              # US$ per million output tokens
  TEACHER_JSON_MODE=1                                 # 1 = ask for a JSON object (DeepSeek supports it)
  MAX_SPEND_USD=15                                    # hard stop for the whole project's API spending
  # optional: JUDGE_BASE_URL / JUDGE_API_KEY / JUDGE_MODEL / JUDGE_PRICE_IN / JUDGE_PRICE_OUT
  #           (a DIFFERENT model family grades better; if unset the judge = the teacher)

EVERY CALL IS LOGGED to workspace/logs/llm_usage.jsonl (tokens and estimated cost), and calls stop
when the total reaches MAX_SPEND_USD. Check it any time:   python llm.py spend
"""
from __future__ import annotations

import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent
_LOCK = threading.Lock()


class BudgetExceeded(RuntimeError):
    pass


def load_env():
    """Read .env from the current folder and the kit folder (does not override real environment variables)."""
    for base in (Path.cwd(), KIT_ROOT):
        p = base / ".env"
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def log_path():
    ws = Path(os.environ.get("SA_WORKSPACE", "workspace"))
    return ws / "logs" / "llm_usage.jsonl"


def total_spend():
    p = log_path()
    if not p.exists():
        return 0.0
    tot = 0.0
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            tot += float(json.loads(line).get("cost", 0))
        except (ValueError, json.JSONDecodeError):
            pass
    return tot


def extract_json(text):
    """Pull the first JSON object/array out of model text (handles ```json fences and chatter)."""
    t = str(text).strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.I).strip()
    dec = json.JSONDecoder()
    for m in re.finditer(r"[\[{]", t):
        try:
            obj, _ = dec.raw_decode(t[m.start():])
            return obj
        except json.JSONDecodeError:
            continue
    raise ValueError("no JSON found in model output")


class Client:
    def __init__(self, prefix="TEACHER", fallback="TEACHER", defaults=None):
        """prefix: which env vars to read (TEACHER_*, JUDGE_*, EVAL_*). fallback: another prefix to use for
        anything unset (the judge falls back to the teacher). Use fallback=None to never fall back (EVAL_*:
        you do not want your local model's calls to be sent to, and billed by, the teacher's provider)."""
        load_env()
        self.prefix = prefix
        dflt = {"BASE_URL": "https://api.deepseek.com", "API_KEY": "", "MODEL": "deepseek-chat", "PRICE_IN": "0.15",
                "PRICE_OUT": "0.60", "JSON_MODE": "0"}
        dflt.update(defaults or {})
        g = lambda k: (os.environ.get(f"{prefix}_{k}")
                       or (os.environ.get(f"{fallback}_{k}") if fallback and prefix != fallback else None) or dflt[k])
        self.base = g("BASE_URL").rstrip("/")
        self.key = g("API_KEY")
        self.model = g("MODEL")
        self.price_in = float(g("PRICE_IN"))
        self.price_out = float(g("PRICE_OUT"))
        self.json_mode = g("JSON_MODE") in ("1", "true", "True")
        self.max_spend = float(os.environ.get("MAX_SPEND_USD", "0") or 0)

    def chat(self, messages, temperature=0.7, max_tokens=4096, json_mode=None, tools=None, tag="",
             retries=6, timeout=300, extra=None):
        """Returns {'text','message','usage','cost'}. Raises BudgetExceeded when MAX_SPEND_USD is reached."""
        if not self.key:
            raise RuntimeError(f"{self.prefix}_API_KEY is not set. Copy .env.example to .env and fill it in.")
        if self.max_spend and total_spend() >= self.max_spend:
            raise BudgetExceeded(f"MAX_SPEND_USD={self.max_spend} reached (spent {total_spend():.2f}).")
        body = {"model": self.model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
        if (self.json_mode if json_mode is None else json_mode):
            body["response_format"] = {"type": "json_object"}
        if tools:
            body["tools"] = tools
        if extra:
            body.update(extra)                       # e.g. {"chat_template_kwargs": {"enable_thinking": False}}
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(f"{self.base}/chat/completions", data=data, method="POST",
                                     headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.key}"})
        last = None
        for attempt in range(retries):
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    out = json.loads(resp.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "ignore")[:300]
                last = f"HTTP {e.code}: {detail}"
                if e.code not in (408, 409, 429, 500, 502, 503, 504):
                    raise RuntimeError(last) from e
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                last = f"network: {e}"
            time.sleep(min(60, 2 ** attempt))
        else:
            raise RuntimeError(f"giving up after {retries} tries: {last}")
        msg = out["choices"][0]["message"]
        usage = out.get("usage", {}) or {}
        pin, pout = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
        cost = (pin * self.price_in + pout * self.price_out) / 1e6
        self._log({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "model": self.model, "tag": tag,
                   "prompt_tokens": pin, "completion_tokens": pout, "cost": round(cost, 6)})
        return {"text": msg.get("content") or "", "message": msg, "usage": usage, "cost": cost}

    def _log(self, row):
        p = log_path()
        with _LOCK:
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "a", encoding="utf-8") as f:
                f.write(json.dumps(row) + "\n")

    def chat_json(self, messages, **kw):
        """chat() + parse the reply as JSON. Returns (obj, result)."""
        r = self.chat(messages, **kw)
        return extract_json(r["text"]), r


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "spend":
        load_env()
        print(f"spent so far: ${total_spend():.4f}  (cap: ${os.environ.get('MAX_SPEND_USD', 'none')})  log: {log_path()}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
