# One-Shot Prompting with a Single Example

## Overview

This project demonstrates **One-Shot Prompting**, a prompt engineering technique where a Large Language Model (LLM) is given **one example** before receiving the actual task. The example teaches the model the expected input and output format, helping it produce more accurate and consistent responses.

In this project, we use the **Groq API** with the **Llama 3.3 70B Versatile** model to classify customer feedback into predefined categories.

---

## Project Structure

```
One-Shot-Prompting/
│
├── venv/
├── .env
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure the API Key

Create a `.env` file in the project folder.

```text
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Groq API key.

---

## Run the Application

```bash
python main.py
```

---

## Expected Output

```
==================================================
ONE-SHOT PROMPTING DEMO
==================================================

Customer Feedback:
"The package arrived two days late, but it was in perfect condition."

Classification:
Delivery

==================================================
```

> **Note:** The exact wording of the classification may vary slightly depending on the model.

---

## What You Will Learn

- Understand the concept of One-Shot Prompting.
- Learn how a single example guides an LLM.
- Use the Groq API to interact with a Large Language Model.
- Observe how a single example improves response consistency.