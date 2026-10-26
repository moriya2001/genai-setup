# Examining Responsible AI Concerns

## Overview

Artificial Intelligence is increasingly used in applications such as recruitment, healthcare, education, finance, and customer service. While AI can improve efficiency and automate decision-making, it can also introduce ethical risks if not designed responsibly.

This project demonstrates how a Large Language Model (LLM) analyses a user prompt to identify potential Responsible AI concerns. The application evaluates the prompt against key Responsible AI principles, highlights potential risks, and provides recommendations for creating fair, transparent, and trustworthy AI systems.

---

## Project Structure

```text
responsible-ai-demo/
│── main.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
```

---

# Project Workflow

```text
               +----------------------+
               |     User Prompt      |
               +----------+-----------+
                          |
                          v
              +-------------------------+
              |  Send Prompt to Groq    |
              |       LLM API           |
              +-----------+-------------+
                          |
                          v
          +----------------------------------+
          | Analyse Responsible AI Principles |
          +----------------+-----------------+
                           |
        +------------------+-------------------+
        |                  |                   |
        v                  v                   v
    Detect Bias      Check Privacy      Evaluate Safety
        |                  |                   |
        +------------------+-------------------+
                           |
                           v
          +----------------------------------+
          | Generate Recommendations & Score |
          +----------------+-----------------+
                           |
                           v
               +--------------------------+
               | Display AI Analysis      |
               +--------------------------+
```

---