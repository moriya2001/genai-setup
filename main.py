import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"


def generate_summary(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


sample_text = """
Artificial Intelligence (AI) is transforming industries across the world by enabling
machines to perform tasks that traditionally required human intelligence. AI is used in
healthcare to assist doctors with diagnosis, in finance to detect fraud, in education to
personalise learning experiences, and in transportation to power autonomous vehicles.
As AI technology continues to evolve, organisations are increasingly adopting AI-driven
solutions to improve efficiency, reduce operational costs, and make data-driven decisions.
However, the rapid growth of AI also raises important concerns regarding privacy,
security, transparency, and ethical use. Governments, researchers, and businesses are
working together to develop responsible AI practices that maximise benefits while
minimising potential risks.
"""

examples = [
    (
        "Example 1: Basic Summary",
        f"""
Summarise the following text in one concise paragraph.

Text:
{sample_text}
"""
    ),
    (
        "Example 2: Bullet-Point Summary",
        f"""
Summarise the following text into five bullet points.

Text:
{sample_text}
"""
    ),
    (
        "Example 3: One-Sentence Summary",
        f"""
Summarise the following text in exactly one sentence.

Text:
{sample_text}
"""
    ),
    (
        "Example 4: Executive Summary",
        f"""
Create an executive summary suitable for business leaders.

Text:
{sample_text}
"""
    ),
    (
        "Example 5: Audience-Specific Summary",
        f"""
Summarise the following text for a 12-year-old student using simple language.

Text:
{sample_text}
"""
    ),
    (
        "Example 6: Summary + Key Takeaways",
        f"""
Read the following text and provide:

1. A short summary.
2. Three key takeaways.
3. One recommended action.

Text:
{sample_text}
"""
    )
]

print("=" * 70)
print("PROMPTING FOR SUMMARISATION")
print("=" * 70)

for title, prompt in examples:
    print(f"\n{title}")
    print("-" * 70)
    print(generate_summary(prompt))

print("\n" + "=" * 70)