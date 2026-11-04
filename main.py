import os
from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ----------------------------------------------------
# Input Text
# ----------------------------------------------------

article = """
Artificial Intelligence is transforming industries by automating repetitive
tasks, improving decision-making, and enabling innovative applications.
"""

# ----------------------------------------------------
# Part 1: Writing Your First Structured Prompt
# ----------------------------------------------------

role = "You are an experienced technical trainer."

task = (
    "Read the text provided and explain it in simple language "
    "suitable for a beginner."
)

context = article

output_format = (
    "Return:\n"
    "1. A short summary.\n"
    "2. Three key points."
)

structured_prompt = f"""
Role:
{role}

Task:
{task}

Context:
{context}

Output Format:
{output_format}
"""

# ----------------------------------------------------
# Part 2: Using Delimiters and Roles in Prompts
# ----------------------------------------------------

delimiter_prompt = f"""
You are an experienced technical trainer.

Read the text enclosed within triple backticks and explain it in simple language suitable for a beginner.

Text: {article}

Return:
1. A short summary.
2. Three key points.
"""

# ----------------------------------------------------
# Send Structured Prompt
# ----------------------------------------------------

structured_response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": structured_prompt
        }
    ],
    temperature=0.3,
)

# ----------------------------------------------------
# Send Delimiter Prompt
# ----------------------------------------------------

delimiter_response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": delimiter_prompt
        }
    ],
    temperature=0.3,
)

# ----------------------------------------------------
# Display Results
# ----------------------------------------------------

print("=" * 70)
print("WRITING YOUR FIRST STRUCTURED PROMPT")
print("=" * 70)

print("\nPROMPT\n")
print(structured_prompt)

print("\nMODEL RESPONSE\n")
print(structured_response.choices[0].message.content)

print("\n" + "=" * 70)
print("USING DELIMITERS AND ROLES IN PROMPTS")
print("=" * 70)

print("\nPROMPT\n")
print(delimiter_prompt)

print("\nMODEL RESPONSE\n")
print(delimiter_response.choices[0].message.content)