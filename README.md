# 🤖 Prompt Engineering with LLM

An interactive Large Language Model (LLM) application that demonstrates different prompt engineering techniques, including Zero-Shot, One-Shot, and Two-Shot prompting. The project explores how prompt design and temperature settings influence AI-generated responses.

## 📌 Project Overview

Prompt engineering is the process of designing and refining prompts to guide Large Language Models toward generating relevant and useful responses.

This project provides a simple interface where users can experiment with different prompting techniques and observe how an LLM responds to the same or similar instructions.

The application is designed for students, beginners, and AI enthusiasts who want to understand how prompt engineering works in practice.

## 🎯 Objectives

* Understand the fundamentals of prompt engineering.
* Implement Zero-Shot, One-Shot, and Two-Shot prompting.
* Explore temperature settings and response variability.
* Learn how to interact with an LLM using Python.
* Build an interactive application using Streamlit.
* Compare outputs generated using different prompting techniques.

## ✨ Features

* **Zero-Shot Prompting:** Generate responses without providing examples.
* **One-Shot Prompting:** Guide the model using one example.
* **Two-Shot Prompting:** Provide two examples to demonstrate the expected response pattern.
* **Temperature Control:** Adjust the temperature parameter to experiment with response variability.
* **Interactive Interface:** Enter prompts and view model-generated responses.
* **Prompt Comparison:** Explore how different prompting approaches affect the output.

## 🛠️ Technologies Used

* Python
* Streamlit
* Large Language Models (LLMs)
* Prompt Engineering
* LLM API or locally configured model

*The exact model and API dependencies depend on your implementation.*

## 📂 Project Structure

```text
Prompt-Engineering-LLM/
│
├── app.py
├── LLM.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File               | Description                                                                      |
| ------------------ | -------------------------------------------------------------------------------- |
| `app.py`           | Implements the Streamlit user interface and prompting options.                   |
| `LLM.py`           | Contains LLM configuration, temperature settings, and response-generation logic. |
| `requirements.txt` | Lists the Python dependencies.                                                   |
| `README.md`        | Documents the project and setup instructions.                                    |
| `.gitignore`       | Excludes virtual environments and sensitive files from Git.                      |

## 🧠 Prompt Engineering Techniques

### 1. Zero-Shot Prompting

Zero-shot prompting asks the model to perform a task without providing examples.

**Example:**

```text
Prompt: Classify the sentiment of this sentence:
"I really enjoyed this movie."

Expected response: Positive
```

### 2. One-Shot Prompting

One-shot prompting provides one example to guide the model.

**Example:**

```text
Example:
Text: "The food was delicious."
Sentiment: Positive

Now classify:
Text: "The service was terrible."
Sentiment:
```

### 3. Two-Shot Prompting

Two-shot prompting provides two examples to demonstrate the expected output pattern.

**Example:**

```text
Example 1:
Text: "I love this product."
Sentiment: Positive

Example 2:
Text: "This product is disappointing."
Sentiment: Negative

Now classify:
Text: "The product works perfectly."
Sentiment:
```

### 4. Temperature in LLMs

Temperature is a parameter that influences the variability of token selection during text generation.

* **Low temperature:** Generally produces more predictable responses.
* **Medium temperature:** Offers a balance between predictability and variability.
* **High temperature:** Generally produces more varied or creative responses.

The effect depends on the model, task, and decoding configuration.

## ⚙️ Installation and Setup

### Prerequisites

Install the following:

* Python 3.10 or a compatible version supported by your dependencies
* Visual Studio Code
* Git
* An API key or local LLM setup, depending on your implementation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Prompt-Engineering-LLM.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Open the Project

```bash
cd Prompt-Engineering-LLM
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
venv\Scripts\activate.bat
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Configure the LLM

Configure the model and credentials required by your implementation.

If using an API key, store it in an environment variable or an appropriate secrets file. Never upload API keys or passwords to GitHub.

### Step 7: Run the Application

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## 🚀 How to Use

1. Start the Streamlit application.
2. Select Zero-Shot, One-Shot, or Two-Shot prompting.
3. Enter your task or prompt.
4. Adjust the temperature if the interface supports it.
5. Generate the response.
6. Compare results across prompting techniques.
7. Observe how examples and generation settings influence the output.

## 📚 Learning Outcomes

By completing this project, users can develop an understanding of:

* Prompt design and optimization.
* Few-shot learning through in-context examples.
* LLM integration with Python.
* Temperature and text-generation behavior.
* Building interactive AI applications.
* Comparing model responses across different prompts.

## 🔮 Future Enhancements

* Add more prompt engineering techniques, including role prompting and prompt chaining.
* Introduce ReAct-style tool-use demonstrations.
* Add side-by-side response comparison.
* Support multiple LLM providers.
* Include response evaluation and prompt testing.
* Add prompt history and export functionality.
* Deploy the application online.

## 🔐 Security

* Never commit API keys or credentials.
* Use environment variables or secure secrets management.
* Add `.env` to `.gitignore` if the project uses a `.env` file.
* Review the model provider's privacy policies before submitting sensitive information.

## 👩‍💻 Author

**Sruthi S**

BSc Computer Science with Artificial Intelligence

Interested in Artificial Intelligence, Generative AI, Large Language Models, and Software Development.

## ⭐ Support

If you find this project useful for learning prompt engineering, consider giving the repository a star on GitHub!

---

**Built with Python, Streamlit, and LLM technology.** 🚀
