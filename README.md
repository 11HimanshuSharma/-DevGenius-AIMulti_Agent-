<!-- @format -->

# 🤖 DevGenius: AI Multi-Agent Development Team

live link :-
[https://devgeniusaimultiagent.streamlit.app/](https://devgeniusaimultiagent.streamlit.app/)

DevGenius is a small web app that acts like an **automated software development
team**.  
You give it a feature request (like _"create a calculator function"_), and a
team of AI agents work together to **write, test, review, and fix the code until
it’s ready**.

It’s designed to **eliminate the slow, back-and-forth process of coding** and
automate the entire development loop.

---

## ❌ The Problem: Coding Can Be a Slow Grind

Writing code isn’t just about typing. Most of the time is spent in a repetitive
feedback cycle:

1. A developer writes some code
2. A reviewer checks it and gives feedback
3. A tester runs it to see if it breaks
4. If there are issues, it goes back to the developer to be fixed

This loop is **essential for quality**, but also a **major bottleneck**.  
**DevGenius tackles this head-on.**

## 🚀 How It Works

The system uses a team of specialized AI agents that collaborate in a loop to
write, review, and refine code.

**Workflow:** `User Request` → **🤵 Manager** (Creates Task) → **👨‍💻 Developer**
(Writes Code) → **🧐 Reviewer** & **🧪 Tester** (Check Code) → **Decision**

- If the code passes, the process is **done**.
- If not, a **🛠️ Refactor Agent** fixes the code, and the loop repeats.

---

## 🛠️ Tech Stack

- **LangGraph** – Enables agent collaboration in a feedback loop
- **LangChain** – Connects agents to the Large Language Model (LLM)
- **Streamlit** – Provides a clean and interactive web interface
- **Python (subprocess & tempfile)** – Creates a safe, temporary sandbox for
  running generated code and tests

---

## 🧠 Choosing the AI Brain

The agents are powered by **LLMs (Large Language Models)**.  
The better the model, the better the results.

- **🌟 Choice: GPT-4o** – Excellent at writing, understanding, and fixing code
- **💡 Free & Practical Choice: Gemini 1.5 Flash** – Great free alternative with
  a massive memory (context window), ideal for the Fixer agent

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- Azure OpenAI API Key and Endpoint

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/11HimanshuSharma/-DevGenius-AIMulti_Agent-.git](https://github.com/11HimanshuSharma/-DevGenius-AIMulti_Agent-.git)
    cd DevGenius-AIMulti_Agent
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:** Copy the `.env.example` file to a new file
    named `.env` and add your Azure OpenAI credentials.

    ```env
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_CHAT_ENDPOINT="[https://your-resource.openai.azure.com/](https://your-resource.openai.azure.com/)"
    AZURE_OPENAI_CHAT_API_KEY="your_api_key"
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

## 🌐 Live Demo

🔗 **Try DevGenius on Streamlit Cloud:**
[https://devgeniusaimultiagent.streamlit.app/](https://devgeniusaimultiagent.streamlit.app/)

---
