# Proprietary vs Open-Source LLM Side by Side

This project compares a **proprietary Large Language Model (Gemini)** with an **open-source Large Language Model (Phi-3)** by sending the same prompts to both models. It allows you to compare their response quality, reasoning ability, coding performance, and inference speed side by side.

---

# Project Structure

```text
proprietary-vs-open-source-llm/
│
├── models/
│   └── model_config.py
│
├── prompts/
│   └── prompts.py
│
├── utils/
│   └── helper.py
│
├── outputs/
│   └── responses.txt
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Technologies

- Python
- Google Gemini API
- Ollama (Phi-3)
- VS Code

---

# Environment Setup

Open the project folder in **Visual Studio Code**.

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Once activated, your terminal should display the virtual environment name.

---

# Install Dependencies

Install all the required Python packages.

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key.

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# Install and Run Ollama

Ensure Ollama is installed on your system.

Download the phi-3 model.

```bash
ollama pull phi3
```

Verify that the model is available.

```bash
ollama list
```

Start the Ollama server if it is not already running.

```bash
ollama serve
```

---

# Run the Application

Execute the application.

```bash
python main.py
```

---

# Output

The application sends the same prompt to both Gemini and Llama 3.2, compares their responses, and displays the results in the terminal.

A copy of all responses is also saved to:

```text
outputs/responses.txt
```

---

# Learning Outcomes

After completing this demo, you will be able to:

- Understand the difference between proprietary and open-source LLMs.
- Compare response quality using identical prompts.
- Evaluate reasoning and coding capabilities.
- Measure inference speed of different models.
- Learn how to integrate multiple LLMs into a single Python application.
- Analyse model outputs side by side for comparison.