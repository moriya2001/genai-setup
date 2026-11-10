# Prompting for Text Classification

## Overview

This project demonstrates how **Prompt Engineering** can be used to perform **Text Classification** using the **Groq API** and a Large Language Model (LLM). Rather than training a machine learning model, the application uses a well-structured prompt to instruct the language model to classify input text into one of several predefined categories. This approach highlights how prompt engineering can enable LLMs to perform classification tasks accurately through natural language instructions alone.

---

## Project Structure

```
Text-Classification-Demo/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env
```

---

## Project Workflow

```text
                  User Enters Text
                          │
                          ▼
              Construct Classification Prompt
                          │
                          ▼
                 Send Prompt to Groq API
                          │
                          ▼
          LLM Analyses the Input Text
                          │
                          ▼
      Predict the Most Suitable Category
                          │
                          ▼
          Display the Classification Result
```

---

## Categories Used

The model classifies the input into one of the following categories:

- Technology
- Sports
- Business
- Entertainment

---