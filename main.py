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

MODEL_NAME = "openai/gpt-oss-120b"

# ----------------------------------------------------
# Few-Shot Prompt
# ----------------------------------------------------

prompt = """
You are an expert sentiment classifier.

Example 1
Text: "The movie was fantastic and full of excitement."
Sentiment: Positive

Example 2
Text: "The food was cold and tasted awful."
Sentiment: Negative

Example 3
Text: "The package arrived on time and was exactly as described."
Sentiment: Positive

Example 4
Text: "Customer support never replied to my emails."
Sentiment: Negative

Now classify the following text.

Text: "The phone has excellent battery life, but the camera quality is disappointing."

Respond using only one word.

Sentiment:
"""

# ----------------------------------------------------
# Generate Response
# ----------------------------------------------------

response = client.chat.completions.create(
    model=MODEL_NAME,
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

print("=" * 60)
print("FEW-SHOT PROMPTING DEMO")
print("=" * 60)

print("\nExamples Provided:")
print("-" * 60)
print("4 labelled sentiment examples")

print("\nInput:")
print("-" * 60)
print('"The phone has excellent battery life, but the camera quality is disappointing."')

print("\nClassification:")
print("-" * 60)
print(response.choices[0].message.content)

print("\n" + "=" * 60)