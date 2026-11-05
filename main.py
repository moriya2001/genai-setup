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

# ----------------------------------------------------
# Initialize Groq Client
# ----------------------------------------------------

client = Groq(api_key=api_key)

# ----------------------------------------------------
# One-Shot Prompt
# ----------------------------------------------------

prompt = """
You are an AI assistant that classifies customer feedback into one of the following categories:

- Billing
- Customer Support
- Product Quality
- Delivery

Example:

Customer Feedback:
"I was charged twice for my subscription this month."

Category:
Billing

Now classify the following customer feedback.

Customer Feedback:
"The package arrived two days late, but it was in perfect condition."

Category:
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

# ----------------------------------------------------
# Display Output
# ----------------------------------------------------

print("=" * 50)
print("ONE-SHOT PROMPTING DEMO")
print("=" * 50)
print()

print("Customer Feedback:")
print('"The package arrived two days late, but it was in perfect condition."')

print("\nClassification:")
print(response.choices[0].message.content.strip())

print()
print("=" * 50)