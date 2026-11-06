# Few-Shot Prompting with an Example Set

This project demonstrates **Few-Shot Prompting**, a prompting technique where multiple input-output examples are included in the prompt to help the language model understand the expected pattern before solving a new task.

## Project Structure

```text
Few-Shot-Prompting-Demo/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure the Environment Variable

Create a `.env` file in the project root directory and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run the Program

```bash
python main.py
```

## Expected Output

The program sends a few labelled examples along with a new input to the language model. Based on the patterns learned from the examples, the model predicts the sentiment of the new text.

Example:

```text
============================================================
FEW-SHOT PROMPTING DEMO
============================================================

Examples Provided:
------------------------------------------------------------
4 labelled sentiment examples

Input:
------------------------------------------------------------
"The phone has excellent battery life, but the camera quality is disappointing."

Classification:
------------------------------------------------------------
Negative

============================================================
```