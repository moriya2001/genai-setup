#  Visualizing Attention in a Transformer

This project demonstrates how the **self-attention mechanism** in a Transformer works by visualizing attention scores as a heatmap. Instead of training a Transformer model, this demo uses a predefined attention matrix to help learners understand how words in a sentence attend to one another.

## Project Structure

```
attention-visualization/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Step 1: Create a Virtual Environment

Open the integrated terminal and run:

```bash
python -m venv venv
```

---

## Step 2: Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

After activation, the terminal should display `(venv)`.

---

## Step 3: Install the Required Libraries

Install the project dependencies using:

```bash
pip install -r requirements.txt
```

This installs:

- NumPy
- Matplotlib
- Seaborn

---

## Step 4: Run the Project

Execute the program with:

```bash
python main.py
```

---

## Expected Output

A heatmap window will appear showing the attention scores between the words in the sentence:

```
The cat sat on the mat
```

- Rows represent **Query** tokens.
- Columns represent **Key** tokens.
- Darker cells indicate higher attention scores.
- Each row represents the attention distribution for one token.
````
