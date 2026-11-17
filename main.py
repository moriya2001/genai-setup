import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------------------------------------
# Load API Key
# -----------------------------------------------------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"

# -----------------------------------------------------
# Function to Call LLM
# -----------------------------------------------------
def generate(prompt):

    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error : {e}"


# -----------------------------------------------------
# Weak Prompt
# -----------------------------------------------------

weak_prompt = """
Explain Artificial Intelligence.
"""

# -----------------------------------------------------
# Improved Prompt (Iteration 1)
# -----------------------------------------------------

iteration1 = """
Explain Artificial Intelligence.

Your explanation should include:

- Definition
- Real-world examples
- Advantages
- Limitations

Keep it under 200 words.
"""

# -----------------------------------------------------
# Improved Prompt (Iteration 2)
# -----------------------------------------------------

iteration2 = """
You are an experienced university professor.

Explain Artificial Intelligence for first-year Computer Science students.

Requirements:

1. Start with a simple definition.
2. Explain how AI works.
3. Give three real-world examples.
4. Mention three advantages.
5. Mention two limitations.
6. End with a short summary.

Use simple English.

Return the answer in Markdown using headings and bullet points.

Maximum 250 words.
"""

# -----------------------------------------------------
# Final Optimized Prompt
# -----------------------------------------------------

final_prompt = """
You are a Computer Science educator creating study material.

Topic:
Artificial Intelligence

Target Audience:
Beginner students

Instructions:

- Use simple language.
- Start with an engaging introduction.
- Explain AI step by step.
- Include three practical examples.
- Add a comparison between AI and traditional programming.
- Mention benefits and challenges.
- End with five key takeaways.

Formatting:

Use Markdown.

Sections should be:

# Introduction

# What is AI?

# How AI Works

# Examples

# AI vs Traditional Programming

# Benefits

# Challenges

# Key Takeaways

Maximum 300 words.
"""

# -----------------------------------------------------
# Execute All Prompt Versions
# -----------------------------------------------------

print("=" * 80)
print("WEAK PROMPT")
print("=" * 80)
print(generate(weak_prompt))

print("\n\n")

print("=" * 80)
print("ITERATION 1")
print("=" * 80)
print(generate(iteration1))

print("\n\n")

print("=" * 80)
print("ITERATION 2")
print("=" * 80)
print(generate(iteration2))

print("\n\n")

print("=" * 80)
print("FINAL OPTIMIZED PROMPT")
print("=" * 80)
print(generate(final_prompt))