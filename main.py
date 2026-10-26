import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print("Error: GROQ_API_KEY not found in the .env file.")
    exit()

URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("=" * 60)
print("      Responsible AI Concerns Analyzer")
print("=" * 60)

user_prompt = input("\nEnter a prompt to analyse: ")

system_prompt = """
You are a Responsible AI expert.

Analyse the user's prompt and identify Responsible AI concerns.

Evaluate the following:
1. Bias
2. Fairness
3. Privacy
4. Harmful Content
5. Hallucination Risk
6. Transparency
7. Accountability

For each concern provide:
- Risk Level
- Explanation
- Recommendation

Finally provide an Overall Responsible AI Score out of 10.
"""

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    "temperature": 0.3
}

try:
    response = requests.post(URL, headers=headers, data=json.dumps(payload))
    response.raise_for_status()

    result = response.json()

    print("\n" + "=" * 60)
    print("Responsible AI Analysis")
    print("=" * 60)
    print(result["choices"][0]["message"]["content"])

except requests.exceptions.RequestException as e:
    print(f"\nAPI Error: {e}")

except Exception as e:
    print(f"\nUnexpected Error: {e}")