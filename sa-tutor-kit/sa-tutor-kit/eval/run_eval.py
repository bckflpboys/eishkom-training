#!/usr/bin/env python3
"""
run_eval.py - give your eval questions to a model and save what it answers.

    # a model served locally (llama.cpp / LM Studio / Ollama / vLLM all speak this protocol):
    python eval/run_eval.py --name base-qwen35-4b --backend openai --base-url http://localhost:8080/v1 --model local
    # a model loaded straight from Hugging Face inside Colab (optionally with your trained LoRA adapter):
    python eval/run_eval.py --name r1-sft --backend hf --model unsloth/Qwen3.5-4B --adapter workspace/runs/r1/adapter
    # the teacher itself (its score is your CEILING: you cannot expect your 4B to beat it):
    TEACHER settings in .env, then  --backend openai --base-url https://api.deepseek.com --api-key-env TEACHER_API_KEY --model deepseek-chat

WHAT IT DOES
  For every item in workspace/eval/eval_items.jsonl it builds the SAME prompt your app will send (the system
  prompt is rendered from the item's control settings by tutor_data.render_system), asks the model, and if the
  model calls a tool it RUNS the tool (tools_sim.py) and lets the model continue - exactly like the app.
  Output: workspace/eval_runs/<name>/outputs.jsonl  (one line per item per sample). Then run score_eval.py.

HOW MANY TIMES? (--n)
  --n 1 --temperature 0     one deterministic answer: for quick regression checks
  --n 5 --temperature 0.7   five samples: measures CONSISTENCY. A model that is right 5/5 times is much
                            more trustworthy than one that is right 3/5. Use this for the decisions that matter.
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import retrieval  # noqa: E402
import tools_sim  # noqa: E402
import board as boardmod  # noqa: E402
import tutor_data as td  # noqa: E402
from llm import Client, load_env  # noqa: E402
from wspaths import append_jsonl, p, read_jsonl  # noqa: E402

THINK_TOKEN_GEMMA = "<|think|>"


# --------------------------------------------------------------------------- parsing model text
def split_thinking(text):
    """'<think>why</think>answer' -> ('why', 'answer'). Unterminated <think> -> everything is reasoning."""
    t = text or ""
    if "</think>" in t:
        before, after = t.split("</think>", 1)
        return before.replace("<think>", "").strip(), after.strip()
    if t.lstrip().startswith("<think>"):
        return t.replace("<think>", "").strip(), ""
    return "", t.strip()


def _coerce(v):
    v = v.strip()
    try:
        return json.loads(v)
    except (json.JSONDecodeError, ValueError):
        return v


def parse_tool_calls_from_text(text):
    """Find <tool_call> blocks in raw model text. Supports the JSON style
       <tool_call>{"name": "x", "arguments": {...}}</tool_call>
    and the XML style
       <tool_call><function=x><parameter=k>v</parameter></function></tool_call>.
    Returns (text_without_blocks, [{"name":..., "arguments": {...}}])."""
    calls = []
    for m in re.finditer(r"<tool_call>(.*?)</tool_call>", text or "", flags=re.S):
        body = m.group(1).strip()
        try:
            obj = json.loads(body)
            args = obj.get("arguments", {})
            calls.append({"name": obj.get("name"), "arguments": json.loads(args) if isinstance(args, str) else args})
            continue
        except (json.JSONDecodeError, AttributeError):
            pass
        f = re.search(r"<function=([^>\n]+)>(.*?)</function>", body, flags=re.S)
        if f:
            args = {k.strip(): _coerce(v) for k, v in re.findall(r"<parameter=([^>\n]+)>\n?(.*?)\n?</parameter>", f.group(2), flags=re.S)}
            calls.append({"name": f.group(1).strip(), "arguments": args})
    clean = re.sub(r"<tool_call>.*?</tool_call>", "", text or "", flags=re.S).strip()
    return clean, calls


# --------------------------------------------------------------------------- backends
class OpenAIBackend:
    def __init__(self, a):
        self.a = a
        key_env = a.api_key_env
        defaults = {"BASE_URL": a.base_url, "API_KEY": os.environ.get(key_env, "local") if key_env else "local",
                    "MODEL": a.model, "PRICE_IN": "0", "PRICE_OUT": "0"}
        self.client = Client("EVAL", fallback=None, defaults=defaults)
        if a.base_url:
            self.client.base = a.base_url.rstrip("/")
        if key_env and os.environ.get(key_env):
            self.client.key = os.environ[key_env]
        self.client.model = a.model

    def generate(self, messages, tools, thinking):
        a = self.a
        msgs = [dict(m) for m in messages]
        extra = None
        if a.think_style == "qwen":
            extra = {"chat_template_kwargs": {"enable_thinking": thinking == "on"}}
        elif a.think_style == "gemma" and thinking == "on" and msgs and msgs[0]["role"] == "system":
            msgs[0]["content"] = THINK_TOKEN_GEMMA + "\n" + msgs[0]["content"]
        r = self.client.chat(self.to_openai(msgs), temperature=a.temperature, max_tokens=a.max_new_tokens, tools=tools or None,
                             json_mode=False, tag=f"eval:{a.name}", extra=extra)
        msg = r["message"]
        reasoning = msg.get("reasoning_content") or msg.get("reasoning") or ""
        text = msg.get("content") or ""
        calls = []
        for tc in msg.get("tool_calls") or []:
            fn = tc.get("function", {})
            args = fn.get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except json.JSONDecodeError:
                    args = {"_raw": args}
            calls.append({"name": fn.get("name"), "arguments": args, "id": tc.get("id")})
        if not calls:                                           # some servers leave tool calls inside the text
            text, calls = parse_tool_calls_from_text(text)
        r2, text = split_thinking(text)
        return {"text": text, "reasoning": reasoning or r2, "tool_calls": calls, "tokens": r["usage"].get("completion_tokens", 0)}

    def image_parts(self, content):
        """Our {"type":"image","path":...} parts -> OpenAI-style image_url parts with the picture inlined (base64)."""
        if not isinstance(content, list):
            return content
        out = []
        for part in content:
            if part.get("type") == "image":
                path = Path(self.a.images_root) / part["path"]
                mime = mimetypes.guess_type(str(path))[0] or "image/png"
                data = base64.b64encode(path.read_bytes()).decode()
                out.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{data}"}})
            else:
                out.append({"type": "text", "text": part.get("text", "")})
        return out

    def to_openai(self, msgs):
        out = []
        for m in msgs:
            m = dict(m)
            m["content"] = self.image_parts(m.get("content"))
            if m.get("tool_calls"):
                m["tool_calls"] = [{"id": tc.get("id") or f"call_{i}", "type": "function",
                                    "function": {"name": tc["function"]["name"] if "function" in tc else tc["name"],
                                                 "arguments": json.dumps((tc["function"]["arguments"] if "function" in tc else tc["arguments"]),
                                                                         ensure_ascii=False)
                                                 if not isinstance((tc["function"]["arguments"] if "function" in tc else tc["arguments"]), str)
                                                 else (tc["function"]["arguments"] if "function" in tc else tc["arguments"])}}
                                   for i, tc in enumerate(m["tool_calls"])]
            out.append(m)
        return out


class HFBackend:
    """Loads a model in this process (use in Colab). Untested against real models in the kit's own test suite:
    if loading fails, copy the model-loading lines from Unsloth's official notebook for your model."""

    def __init__(self, a):
        import torch
        self.torch = torch
        self.a = a
        self.loader = a.loader
        if self.loader == "auto":
            try:
                import unsloth  # noqa: F401
                self.loader = "unsloth"
            except ImportError:
                self.loader = "hf"
        if self.loader == "unsloth":
            from unsloth import FastLanguageModel
            name = a.adapter or a.model                    # an adapter folder loads its base model automatically
            kw = dict(model_name=name, max_seq_length=a.max_seq_length, load_in_4bit=a.load_4bit)
            try:
                self.model, self.tok = FastLanguageModel.from_pretrained(**kw, load_in_16bit=not a.load_4bit)
            except TypeError:
                self.model, self.tok = FastLanguageModel.from_pretrained(**kw)
            FastLanguageModel.for_inference(self.model)
        else:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            self.tok = AutoTokenizer.from_pretrained(a.model)
            kw = dict(torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16, device_map="auto")
            if a.load_4bit:
                from transformers import BitsAndBytesConfig
                kw = dict(quantization_config=BitsAndBytesConfig(load_in_4bit=True), device_map="auto")
            self.model = AutoModelForCausalLM.from_pretrained(a.model, **kw)
            if a.adapter:
                from peft import PeftModel
                self.model = PeftModel.from_pretrained(self.model, a.adapter)
            self.model.eval()

    def generate(self, messages, tools, thinking):
        a = self.a
        msgs = []
        for m in messages:
            m = dict(m)
            if m.get("tool_calls"):                                       # HF templates want dict arguments
                m["tool_calls"] = [{"type": "function", "function": {
                    "name": tc["function"]["name"] if "function" in tc else tc["name"],
                    "arguments": (lambda x: json.loads(x) if isinstance(x, str) else x)(tc["function"]["arguments"] if "function" in tc else tc["arguments"])}}
                    for tc in m["tool_calls"]]
            msgs.append(m)
        kw = {}
        if a.think_style == "qwen":
            kw["enable_thinking"] = thinking == "on"
        elif a.think_style == "gemma" and thinking == "on" and msgs and msgs[0]["role"] == "system":
            msgs[0]["content"] = THINK_TOKEN_GEMMA + "\n" + msgs[0]["content"]
        prompt = self.tok.apply_chat_template(msgs, tools=tools or None, tokenize=False, add_generation_prompt=True, **kw)
        inputs = self.tok(prompt, return_tensors="pt", add_special_tokens=False).to(self.model.device)
        gen_kw = dict(max_new_tokens=a.max_new_tokens, pad_token_id=self.tok.eos_token_id)
        if a.temperature > 0:
            gen_kw.update(do_sample=True, temperature=a.temperature, top_p=0.95)
        else:
            gen_kw.update(do_sample=False)
        with self.torch.no_grad():
            out = self.model.generate(**inputs, **gen_kw)
        new = out[0][inputs["input_ids"].shape[1]:]
        raw = self.tok.decode(new, skip_special_tokens=False)
        raw = re.sub(r"<\|im_end\|>|<\|endoftext\|>|<end_of_turn>|<eos>", "", raw).strip()
        # the template may already have opened <think>: re-add the tag so split_thinking sees it
        if prompt.rstrip().endswith("<think>") and "</think>" in raw:
            raw = "<think>" + raw
        text, calls = parse_tool_calls_from_text(raw)
        reasoning, text = split_thinking(text)
        return {"text": text, "reasoning": reasoning, "tool_calls": calls, "tokens": int(new.shape[0])}


# --------------------------------------------------------------------------- one item, with tool loop
def answer_item(backend, item, fields, index, max_rounds, thinking_override):
    control = item["control"]
    thinking = thinking_override if thinking_override != "auto" else item.get("thinking", "off")
    msgs = [{"role": "system", "content": td.render_system(control, fields)}] + [dict(m) for m in item["messages"]]
    tools = [td.TOOL_REGISTRY[t] for t in control.get("tools", [])]
    bd = boardmod.Board()
    all_calls, all_results, reasonings, tokens = [], [], [], 0
    final = ""
    t0 = time.time()
    for rnd in range(max_rounds):
        out = backend.generate(msgs, tools, thinking)
        tokens += out["tokens"]
        if out["reasoning"]:
            reasonings.append(out["reasoning"])
        if out["tool_calls"]:
            calls = []
            for k, tc in enumerate(out["tool_calls"]):
                calls.append({"id": tc.get("id") or f"call_{rnd}_{k}", "type": "function",
                              "function": {"name": tc["name"], "arguments": tc["arguments"]}})
            msgs.append({"role": "assistant", "content": out["text"], "tool_calls": calls})
            for tc in calls:
                name, args = tc["function"]["name"], tc["function"]["arguments"]
                all_calls.append({"name": name, "arguments": args})
                res = tools_sim.run_tool(name, args if isinstance(args, dict) else {}, bd, index) if name in control.get("tools", []) else None
                res = res if res is not None else "ERROR: that tool is not available."
                all_results.append(res)
                msgs.append({"role": "tool", "name": name, "tool_call_id": tc["id"], "content": res})
            continue
        final = out["text"]
        break
    return {"text": final, "reasoning": "\n---\n".join(reasonings), "tool_calls": all_calls, "tool_results": all_results,
            "rounds": rnd + 1, "tokens": tokens, "latency_s": round(time.time() - t0, 2), "thinking": thinking}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="run name; outputs go to workspace/eval_runs/<name>/")
    ap.add_argument("--backend", choices=["openai", "hf"], required=True)
    ap.add_argument("--model", default="local")
    ap.add_argument("--base-url", default=os.environ.get("EVAL_BASE_URL", "http://localhost:8080/v1"))
    ap.add_argument("--api-key-env", default="EVAL_API_KEY", help="name of the environment variable holding the key")
    ap.add_argument("--adapter", help="hf backend: folder with your trained LoRA adapter")
    ap.add_argument("--loader", choices=["auto", "unsloth", "hf"], default="auto")
    ap.add_argument("--load-4bit", action="store_true", help="hf backend: load in 4-bit (for auditioning big models on a small GPU)")
    ap.add_argument("--max-seq-length", type=int, default=4096)
    ap.add_argument("--items", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--tags", nargs="*", help="only items with any of these tags (e.g. core maths)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--n", type=int, default=1, help="samples per item")
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--max-new-tokens", type=int, default=1500)
    ap.add_argument("--thinking", choices=["auto", "on", "off"], default="auto", help="auto = what each item says")
    ap.add_argument("--think-style", choices=["qwen", "gemma", "none"], default="qwen",
                    help="how this model switches thinking: qwen = chat-template flag, gemma = a token in the system prompt")
    ap.add_argument("--render-fields", default="all", help="control fields to show in the system prompt (comma list or all)")
    ap.add_argument("--max-rounds", type=int, default=3, help="max model<->tool round trips per item")
    ap.add_argument("--images-root", default=str(p("images")), help="folder that image paths in eval items are relative to")
    a = ap.parse_args()
    load_env()                                   # so --api-key-env TEACHER_API_KEY finds the key in .env

    items = read_jsonl(a.items)
    if a.tags:
        items = [i for i in items if set(i.get("tags", [])) & set(a.tags)]
    if a.limit:
        items = items[: a.limit]
    fields = set(td.OPTIONAL_RENDER) if a.render_fields == "all" else {f.strip() for f in a.render_fields.split(",")}
    index = retrieval.load_index(p("index", "bm25.json")) if p("index", "bm25.json").exists() else None
    out_path = p("eval_runs", a.name, "outputs.jsonl")
    done = {(r["id"], r["sample"]) for r in read_jsonl(out_path)} if out_path.exists() else set()
    backend = OpenAIBackend(a) if a.backend == "openai" else HFBackend(a)

    total = len(items) * a.n
    k = 0
    for item in items:
        for s in range(a.n):
            k += 1
            if (item["id"], s) in done:
                continue
            try:
                res = answer_item(backend, item, fields, index, a.max_rounds, a.thinking)
            except Exception as e:                                           # noqa: BLE001
                res = {"text": "", "reasoning": "", "tool_calls": [], "tool_results": [], "rounds": 0, "tokens": 0,
                       "latency_s": 0, "thinking": a.thinking, "error": f"{type(e).__name__}: {e}"[:300]}
            res.update({"id": item["id"], "sample": s, "run": a.name})
            append_jsonl(out_path, res)
            print(f"[{k}/{total}] {item['id']} s{s}: {res.get('error') or res['text'][:70].replace(chr(10), ' ')}")
    meta = {"name": a.name, "backend": a.backend, "model": a.model, "adapter": a.adapter, "n": a.n, "temperature": a.temperature,
            "thinking": a.thinking, "think_style": a.think_style, "items": len(items), "created": time.strftime("%Y-%m-%d %H:%M")}
    (out_path.parent / "run.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"\nwrote {out_path}\nNEXT: python eval/score_eval.py --name {a.name}")


if __name__ == "__main__":
    main()
