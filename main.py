import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in the .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("=" * 50)
print("      Text Generation with Gemini")
print("=" * 50)

while True:
    prompt = input("\nEnter your prompt (type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("\nThank you for using Gemini!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        print("\nGenerated Response:\n")
        print(response.text)

    except Exception as error:
        print(f"\nError: {error}")