import os
import requests
from dotenv import load_dotenv

from groq import Groq
from google import genai
from openai import OpenAI

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------
load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")
openrouter_key = os.getenv("OPENROUTER_API_KEY")
nvidia_key = os.getenv("NVIDIA_API_KEY")

# ---------------------------------------------------
# Clients
# ---------------------------------------------------

groq_client = Groq(api_key=groq_key)

gemini_client = genai.Client(api_key=gemini_key)

openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_key
)

# ---------------------------------------------------
# Structured Prompt
# ---------------------------------------------------

print("=" * 70)
print("        Writing Your First Structured Prompt")
print("=" * 70)

topic = input("\nEnter a topic: ").strip()

if not topic:
    print("Topic cannot be empty.")
    exit()

prompt = f"""
You are an expert educator.

Task:
Explain the topic: {topic}

Instructions:
1. Give a simple definition.
2. Explain why it is important.
3. Explain how it works.
4. Give one real-world example.
5. List three key takeaways.

Use headings.
Use bullet points.
Keep the explanation beginner friendly.
Limit the response to about 250 words.
"""

# ---------------------------------------------------
# Groq
# ---------------------------------------------------

try:
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    print("\n" + "=" * 70)
    print("Groq - Llama 3.3 70B")
    print("=" * 70)
    print(response.choices[0].message.content)

except Exception as e:
    print("\nGroq Error:", e)

# ---------------------------------------------------
# Gemini
# ---------------------------------------------------

try:

    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    print("\n" + "=" * 70)
    print("Gemini 3.5 Flash")
    print("=" * 70)
    print(response.text)

except Exception as e:
    print("\nGemini Error:", e)

# ---------------------------------------------------
# OpenRouter
# ---------------------------------------------------

try:

    response = openrouter_client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    print("\n" + "=" * 70)
    print("OpenRouter - GPT OSS")
    print("=" * 70)
    print(response.choices[0].message.content)

except Exception as e:
    print("\nOpenRouter Error:", e)

# ---------------------------------------------------
# NVIDIA NIM
# ---------------------------------------------------

try:

    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {nvidia_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "minimaxai/minimax-m3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.5,
        "max_tokens": 1024
    }

    response = requests.post(
        invoke_url,
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    print("\n" + "=" * 70)
    print("NVIDIA NIM - MiniMax M3")
    print("=" * 70)
    print(data["choices"][0]["message"]["content"])

except Exception as e:
    print("\nNVIDIA Error:", e)

print("\n" + "=" * 70)
print("Comparison Complete")
print("=" * 70)