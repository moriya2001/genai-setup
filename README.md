# Exploring Tokenization

A simple Python demonstration that explains how tokenization works in Large Language Models (LLMs) using the Hugging Face Transformers library.

## Project Structure

Tokenization-Demo/
│
├── venv/
├── tokenizer_demo.py
├── requirements.txt
├── README.md
└── .gitignore

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Execute the following command:

```bash
python tokenizer_demo.py
```

## Example

### Input

```
Hello, welcome to Generative AI.
```

### Output

```
Tokens:
['Hello', ',', 'Ġwelcome', 'Ġto', 'ĠGener', 'ative', 'ĠAI', '.']

Token IDs:
[15496, 11, 7062, 284, 402, 1223, 9552, 13]

Total Tokens:
8
```