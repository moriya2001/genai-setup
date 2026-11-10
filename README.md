# Prompting for Summarisation

## Overview

This project demonstrates how prompt engineering can be used to generate summaries in different formats using the Groq API and the Llama 3.3 70B Versatile model. Although the source text remains the same, changing the prompt allows the Large Language Model (LLM) to produce summaries with varying levels of detail, structure, and intended audience.

The project illustrates how effective prompt design can significantly influence the quality and presentation of AI-generated summaries.

---

## Project Structure

```
Prompting_for_Summarisation/
│── main.py              # Main application containing summarisation prompts
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
│── .gitignore           # Files ignored by Git
│── .env                 # Stores the Groq API key
```

---

## Project Workflow

```
                +----------------------+
                |   Input Text         |
                +----------+-----------+
                           |
                           v
               +------------------------+
               | Prompt Engineering     |
               | (Different Prompts)    |
               +----------+-------------+
                          |
                          v
                +----------------------+
                |  Groq API            |
                | Llama 3.3 70B Model  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | AI Generated Summary |
                +----------+-----------+
                           |
                           v
        +---------------------------------------+
        | Display Results in the Terminal       |
        +---------------------------------------+
```

---
