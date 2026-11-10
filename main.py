import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "openai/gpt-oss-120b"


def classify_text(text: str) -> str:
    prompt = f"""
You are a text classification assistant.

Classify the given text into exactly ONE of the following categories:

- Technology
- Sports
- Business
- Entertainment

Rules:
1. Return ONLY the category name.
2. Do not explain your answer.
3. Do not generate additional text.

Text:
\"\"\"{text}\"\"\"
"""

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

    return response.choices[0].message.content.strip()


def main():
    print("=" * 60)
    print("TEXT CLASSIFICATION DEMO")
    print("=" * 60)

    text = input("\nEnter text to classify:\n\n")

    category = classify_text(text)

    print("\nPredicted Category:")
    print(category)

    print("=" * 60)


if __name__ == "__main__":
    main()