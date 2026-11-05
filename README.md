# Zero-Shot Prompting in Practice

## Overview

This project demonstrates **Zero-Shot Prompting**, where a Large Language Model completes a task using only the user's instruction without any examples.

## Requirements

- Python 3.10 or later
- Groq API Key

## Installation

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Environment

Open the `.env` file and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL=llama-3.3-70b-versatile
```

### 5. Run the Application

```bash
python main.py
```

## Example

**Input**

```
Explain Artificial Intelligence in simple terms.
```

**Output**

```
Artificial Intelligence (AI) enables computers to perform tasks that normally require human intelligence, such as learning, understanding language, solving problems, and making decisions. It powers technologies like chatbots, recommendation systems, voice assistants, and self-driving cars.
```