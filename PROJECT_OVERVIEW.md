# 🚀 DevGenius: Your Automated AI Software Development Team

DevGenius is a small web app that acts like an **automated software development team**.  
You give it a feature request (like *"create a calculator function"*), and a team of AI agents work together to **write, test, review, and fix the code until it’s ready**.  

It’s designed to **eliminate the slow, back-and-forth process of coding** and automate the entire development loop.

---

## ❌ The Problem: Coding Can Be a Slow Grind
Writing code isn’t just about typing. Most of the time is spent in a repetitive feedback cycle:

1. A developer writes some code  
2. A reviewer checks it and gives feedback  
3. A tester runs it to see if it breaks  
4. If there are issues, it goes back to the developer to be fixed  

This loop is **essential for quality**, but also a **major bottleneck**.  
**DevGenius tackles this head-on.**

---

## ✅ The Solution: An AI Team That Works for You
DevGenius uses a team of specialized **AI agents** that mimic a real-world dev team.  
The entire process is **automated in a continuous loop**:

- 🤵 **Project Manager** → Turns your simple request into a detailed coding task  
- 👨‍💻 **Coder** → Writes the first draft of the Python code  
- 🧐 **Reviewer** → Reviews the code for bugs, style issues, and potential problems  
- 🧪 **Tester** → Writes and runs `pytest` tests to check correctness and edge cases  
- 🛠️ **Fixer (Refactor Agent)** → Fixes issues found by the Reviewer or Tester and improves the code  

If issues are found, the code is **sent back through the loop** until it’s fixed (or a maximum number of tries is reached).

---

## 🛠️ Tech Stack
- **LangGraph** – Enables agent collaboration in a feedback loop  
- **LangChain** – Connects agents to the Large Language Model (LLM)  
- **Streamlit** – Provides a clean and interactive web interface  
- **Python (subprocess & tempfile)** – Creates a safe, temporary sandbox for running generated code and tests  

---

## 🧠 Choosing the AI Brain
The agents are powered by **LLMs (Large Language Models)**.  
The better the model, the better the results.

- **🌟 Dream Choice: GPT-4o** – Excellent at writing, understanding, and fixing code  
- **💡 Free & Practical Choice: Gemini 1.5 Flash** – Great free alternative with a massive memory (context window), ideal for the Fixer agent  


