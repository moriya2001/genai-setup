import os
from dotenv import load_dotenv
from groq import Groq

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: GROQ_API_KEY not found in the .env file.")
    print("Create a .env file and add:")
    print("GROQ_API_KEY=your_api_key_here")
    exit()

# --------------------------------------------------
# Initialize Groq Client
# --------------------------------------------------
client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"

# --------------------------------------------------
# Reusable Prompt Template
# --------------------------------------------------
PROMPT_TEMPLATE = """
You are an expert AI assistant.

Perform the following task carefully.

Task:
{task}

Input:
{text}

Instructions:
- Follow the task exactly.
- Keep the response clear and well structured.
- Do not add unnecessary explanations unless requested.
- Return only the final answer.
"""

# --------------------------------------------------
# User Input
# --------------------------------------------------
print("=" * 70)
print("        BUILDING A REUSABLE PROMPT TEMPLATE")
print("=" * 70)

task = input("\nEnter the task (Summarize, Translate, Explain, etc.): ").strip()

print("\nEnter the input text:")
text = input("> ").strip()

if not task:
    print("\nTask cannot be empty.")
    exit()

if not text:
    print("\nInput text cannot be empty.")
    exit()

# --------------------------------------------------
# Fill Prompt Template
# --------------------------------------------------
prompt = PROMPT_TEMPLATE.format(
    task=task,
    text=text
)

print("\nGenerating response...\n")

# --------------------------------------------------
# Call Groq API
# --------------------------------------------------
try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=512
    )

    print("=" * 70)
    print("AI RESPONSE")
    print("=" * 70)
    print(response.choices[0].message.content)

except Exception as e:
    print("\nAn error occurred while calling the Groq API.")
    print(e)