import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

# Create Groq client
client = Groq(api_key=API_KEY)

MODEL = "openai/gpt-oss-120b"


def ask_llm(prompt):
    """Send a prompt to the Groq API and return the response."""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


def main():

    print("=" * 60)
    print("CHAIN-OF-THOUGHT PROMPTING DEMO")
    print("=" * 60)

    question = input("\nEnter a reasoning question: ")

    # Standard Prompt
    basic_prompt = f"""
Answer the following question as briefly as possible.

Question:
{question}
"""

    # Structured Reasoning Prompt
    reasoning_prompt = f"""
Solve the following problem using a structured reasoning approach.

Question:
{question}

Provide your response using the following format:

## Important Information
List the key facts.

## Step-by-Step Solution
Explain the solution in a logical sequence.

## Final Answer
Provide only the final answer.
"""

    print("\nGenerating standard response...\n")
    standard_response = ask_llm(basic_prompt)

    print("-" * 60)
    print("STANDARD PROMPT")
    print("-" * 60)
    print(standard_response)

    print("\nGenerating structured reasoning response...\n")
    structured_response = ask_llm(reasoning_prompt)

    print("-" * 60)
    print("CHAIN-OF-THOUGHT PROMPT")
    print("-" * 60)
    print(structured_response)


if __name__ == "__main__":
    main()