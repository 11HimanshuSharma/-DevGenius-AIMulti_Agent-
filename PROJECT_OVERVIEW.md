I built a small web app called DevGenius that acts like an automated software development team. You give it a feature request (like "create a calculator function"), and a team of AI agents work together to write, test, and fix the code until it's ready. It's designed to automate the slow, back-and-forth process of coding.

1. The Problem: Coding Can Be a Slow Grind
Writing code isn't just about typing. A huge amount of time is spent on a repetitive cycle:

A developer writes some code.

It goes to a reviewer for feedback.

It goes to a tester to see if it breaks.

If there are issues, it goes back to the developer to be fixed.

This feedback loop is essential for quality, but it's also a major bottleneck. My project tackles this head-on.

2. My Solution: An AI Team That Does the Work for You
DevGenius uses a team of specialized AI agents that mimic a real-world dev team. The entire process is automated in a continuous loop.

Here’s how the team works together:

🤵 The Project Manager: You give it a simple request. It turns that into a clear, detailed task for the Coder.

👨‍💻 The Coder: Gets the task and writes the first draft of the Python code.

🧐 The Reviewer: Scans the code for bugs, style issues, and potential problems. It provides feedback just like a senior developer would.

🧪 The Tester: Writes and runs pytest tests to check if the code actually works and handles edge cases.

🛠️ The Fixer (Refactor Agent): If the Reviewer or Tester finds any issues, this agent takes their feedback and the broken code, then writes an improved version.

This new version doesn't get a free pass—it's sent right back to the Reviewer and Tester. This loop continues until the code is perfect or it hits a set number of tries.

3. The Tech Stack (What's Under the Hood)
I used a few key tools to bring this to life:

LangGraph: The most important tool. It let me create the feedback loop where agents can send work back and forth. A simple linear tool wouldn't work for this.

LangChain: The bridge that connects my agents to the Large Language Model (LLM), allowing them to think and write.

Streamlit: A super simple Python library for building the web interface you see. Perfect for making quick, interactive demos.

Python (subprocess & tempfile): Used to create a safe, temporary "sandbox" to run the generated code and tests without any security risks.

4. Choosing the Right AI Brain (The LLM)
The quality of the agents depends entirely on the LLM powering them.

The Dream Choice: GPT-4o
For a real-world application, this is the best choice. It's incredibly smart at writing, understanding, and fixing code, which is exactly what my Coder, Reviewer, and Fixer agents need.

The Free & Practical Choice: Gemini 1.5 Flash
This is a fantastic free alternative. Its key feature is a massive "memory" (context window), which is perfect for the Fixer agent—it can look at the original code, the review comments, and the test results all at once to make a smart fix.

5. Code & Demo
GitHub Repo: https://github.com/your-username/devgenius-ai-agent-team (Placeholder link)

Live Demo: https://devgenius-demo.streamlit.app (Placeholder link)
