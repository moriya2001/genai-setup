# Building a Reusable Prompt Template

## Overview

This project demonstrates how to build a **reusable prompt template** using the **Groq API** and the **Llama 3.3 70B Versatile** model.

Rather than writing a completely new prompt for every request, a reusable template allows you to define a consistent prompt structure with placeholders that can be dynamically filled with different tasks and inputs. This approach makes prompt engineering more efficient, scalable, and easier to maintain.

---

# Project Structure

```text
reusable-prompt-template/
│
├── main.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Project Workflow

```
                User Starts the Program
                         │
                         ▼
             Enter the Required Task
     (Summarize / Translate / Explain)
                         │
                         ▼
                Enter the Input Text
                         │
                         ▼
       Fill the Reusable Prompt Template
        (Replace Task and Text Placeholders)
                         │
                         ▼
          Send Prompt to the Groq API
                         │
                         ▼
      Llama 3.3 70B Processes the Prompt
                         │
                         ▼
           Generate the Requested Output
                         │
                         ▼
          Display the AI Response
```

---

