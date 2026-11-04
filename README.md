# Controlling Output Format with Prompts

## Overview

This video demonstrates how prompt instructions can control the format of an AI model's response. The same topic is presented in different output formats based solely on the prompt provided to the model.

## Files

```text
controlling-output-format/
│
├── .env
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

## Setup

### 1. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
```

**macOS/Linux**

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**Windows (Command Prompt)**

```bash
venv\Scripts\activate
```

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project directory and add your Groq API key.

```text
GROQ_API_KEY=your_api_key_here
```

## 5. Running the Project

Run the application using:

```bash
python main.py
```

## How the Project Works

1. Enter a topic.
2. Select the desired output format.
3. The application creates a prompt based on your selection.
4. The prompt is sent to the Groq API using the Llama model.
5. The model generates the response in the requested format.

## Available Output Formats

- Paragraph
- Bullet Points
- Markdown Table
- JSON
- HTML

## Example

**Input**

```text
Topic:
Artificial Intelligence

Format:
Bullet Points
```

**Output**

```text
• Artificial Intelligence enables machines to perform tasks that typically require human intelligence.
• AI is widely used in healthcare, finance, education, and transportation.
• Machine learning is a major branch of AI.
• AI improves productivity by automating repetitive tasks.
```