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

print("=" * 60)
print("Demo: Controlling Output Format with Prompts")
print("=" * 60)

topic = input("\nEnter a topic: ")

formats = {
    "1": "Write a short paragraph about the topic.",
    "2": "Write the information as bullet points.",
    "3": "Present the information as a Markdown table with two columns: Aspect and Description.",
    "4": "Return the information in valid JSON format.",
    "5": "Return the information in HTML format."
}

print("\nChoose an output format:")
print("1. Paragraph")
print("2. Bullet Points")
print("3. Markdown Table")
print("4. JSON")
print("5. HTML")

choice = input("\nEnter your choice (1-5): ")

instruction = formats.get(choice)

if instruction:
    prompt = f"""
{instruction}

Topic: {topic}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
    )

    print("\nGenerated Output:\n")
    print(response.choices[0].message.content)

else:
    print("Invalid choice.")