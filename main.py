import os
from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

model = os.getenv("MODEL", "openai/gpt-oss-120b")

# ----------------------------------------------------
# Initialize Groq Client
# ----------------------------------------------------

client = Groq(api_key=api_key)

print("=" * 60)
print("ZERO-SHOT PROMPTING DEMO")
print("=" * 60)

prompt = input("\nEnter your prompt: ")

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAI Response:\n")
print(response.choices[0].message.content)