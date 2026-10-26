# Import the list of prompts
from prompts.prompts import PROMPTS

# Import both language models
from models.model_config import ask_gemini, ask_phi

# Import helper function
from utils.helper import compare


with open("outputs/responses.txt", "w", encoding="utf-8") as file:

    for prompt in PROMPTS:

        gemini_response, phi_response = compare(
            prompt,
            ask_gemini,
            ask_phi
        )

        file.write("=" * 100 + "\n")
        file.write(f"PROMPT\n{prompt}\n\n")

        file.write("PROPRIETARY MODEL (Gemini 3.6 Flash)\n")
        file.write("-" * 80 + "\n")
        file.write(gemini_response + "\n\n")

        file.write("OPEN-SOURCE MODEL (Phi-3)\n")
        file.write("-" * 80 + "\n")
        file.write(phi_response + "\n\n")