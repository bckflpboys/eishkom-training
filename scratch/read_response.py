import json

transcript_path = r"C:\Users\Admin\.gemini\antigravity\brain\d63a603b-b01d-47d3-afc4-d6741b1c1ba3\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        if idx in range(3681, 3700):
            content = data.get("content")
            if content and not data.get("tool_calls") and data.get("source") == "MODEL":
                print(f"Step {idx}:")
                print(content)
                print("=" * 60)

