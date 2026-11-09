import os
from dotenv import load_dotenv

from groq import Groq
from openai import OpenAI
from google import genai

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# API Clients
# ==========================================================

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

openrouter_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

nvidia_client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

# ==========================================================
# Context
# ==========================================================

context = """
Artificial Intelligence (AI) is a branch of computer science focused on
building systems capable of performing tasks that normally require human
intelligence such as reasoning, learning, decision making, language
understanding, and problem solving.

Machine Learning (ML) is a subset of Artificial Intelligence. Instead of
being explicitly programmed, Machine Learning algorithms learn patterns
from data and improve their performance over time.

Deep Learning is a specialized branch of Machine Learning that uses
artificial neural networks with multiple hidden layers. It is widely used
in image recognition, speech recognition, natural language processing,
robotics, and autonomous vehicles.

Large Language Models (LLMs) are Deep Learning models trained on enormous
amounts of text. They can answer questions, generate content, summarize
documents, write code, and assist with reasoning tasks.
"""

print("=" * 80)
print("PROMPT ENGINEERING DEMO")
print("Prompting for Question Answering")
print("=" * 80)

question = input("\nEnter your question: ")

prompt = f"""
You are an intelligent Question Answering Assistant.

Read the context carefully before answering.

Instructions:

- Answer ONLY using the provided context.
- Do NOT use outside knowledge.
- Explain the answer naturally in your own words.
- Do NOT copy the context sentence by sentence.
- Keep the answer between 40 and 80 words.
- If the answer is unavailable, reply exactly:

I don't know based on the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

# ==========================================================
# Function
# ==========================================================

def print_response(title, func):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    try:
        print(func())
    except Exception as e:
        print("Error:", e)

# ==========================================================
# Groq
# ==========================================================

def groq_response():
    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# ==========================================================
# OpenRouter
# ==========================================================

def openrouter_response():
    response = openrouter_client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=250
    )

    return response.choices[0].message.content

# ==========================================================
# Gemini
# ==========================================================

def gemini_response():
    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text

# ==========================================================
# NVIDIA MiniMax M3
# ==========================================================

def nvidia_response():
    response = nvidia_client.chat.completions.create(
        model="minimaxai/minimax-m3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        top_p=0.95,
        max_tokens=250
    )

    return response.choices[0].message.content

# ==========================================================
# Execute
# ==========================================================

print_response("Groq (Llama 3.3 70B)", groq_response)

print_response("OpenRouter (GPT-OSS-20B Free)", openrouter_response)

print_response("Gemini 3.5 Flash", gemini_response)

print_response("NVIDIA NIM (MiniMax M3)", nvidia_response)

print("\n" + "=" * 80)
print("Comparison Completed Successfully")
print("=" * 80)