import subprocess

with open('workspace/scratch/test_gemma_clean.py', 'r', encoding='utf-8') as f:
    code = f.read()

models = [
    'models/gemini-flash-lite-latest',
    'models/gemini-3.1-flash-lite',
    'models/gemma-4-26b-a4b-it'
]

for m in models:
    print(f"\n==================== Testing {m} ====================")
    test_code = code.replace('model_name = "models/gemma-4-31b-it"', f'model_name = "{m}"')
    with open('workspace/scratch/test_tmp.py', 'w', encoding='utf-8') as f:
        f.write(test_code)
    res = subprocess.run(['python', 'workspace/scratch/test_tmp.py'], capture_output=True, text=True)
    print("STDOUT:\n", res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr[:300])
    if "SUCCESS" in res.stdout:
        print(f"*** {m} WON! Extraction is verified! ***")
        break

