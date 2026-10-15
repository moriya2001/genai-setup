# Text Generation with Gemini
## Installation
### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure the API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python main.py
```

---

## Example

Input:

```
Explain Artificial Intelligence.
```

Output:

```
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and understanding language.
```

---

## Project Structure

Text-Generation-Demo/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py