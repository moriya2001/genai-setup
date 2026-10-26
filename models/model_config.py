import os
from dotenv import load_dotenv
from google import genai
from ollama import Client

load_dotenv()

# -----------------------------
# Gemini Configuration
# -----------------------------
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# Ollama Configuration
# -----------------------------
ollama_client = Client(host="http://127.0.0.1:11434")


def ask_gemini(prompt: str) -> str:
    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"


def ask_phi(prompt: str) -> str:
    try:
        response = ollama_client.chat(
            model="phi3:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Phi-3 Error: {e}"