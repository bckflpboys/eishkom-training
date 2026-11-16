import json

transcript_path = r"C:\Users\Admin\.gemini\antigravity\brain\d63a603b-b01d-47d3-afc4-d6741b1c1ba3\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            content = data.get("content", "")
            lower = content.lower()
            if any(term in lower for term in ["1b", "stage 3", "stage-3", "round 3", "baby jake", "baby-jake", "distill", "celeron"]):
                print(f"Step {data.get('step_index')}:")
                print(content)
                print("-" * 50)

