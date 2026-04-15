# 🚀 AI Accessibility Agent (React + WCAG)

An AI-powered tool that scans React applications and suggests fixes to achieve WCAG accessibility compliance.

## ✨ Features

* 🔍 Detects accessibility issues (WCAG 2.2)
* 🤖 AI-powered fix suggestions
* 📂 Multi-file React project scanning
* ⚡ Rule-based + AI hybrid system
* 🧠 Developer-friendly output with code snippets

## 🧱 Tech Stack

* Python (FastAPI-ready)
* Node.js (Babel for JSX parsing)
* OpenAI API (for AI fixes)

## 🧪 Example Issues Detected

* Missing alt text
* Non-semantic clickable elements
* Missing form labels
* Incorrect tabIndex usage
* ARIA misuse

## ▶️ How to Run

```bash
# install dependencies
pip install -r requirements.txt
npm install

# run scanner
python -m agents.react_accessibility.scanner_agent
```

## 📸 Sample Output

```
File: App.jsx
Issue: Image missing alt text

❌ Original:
<img src="logo.png" />

✅ Suggested Fix:
<img src="logo.png" alt="Company logo" />
```
## 📸 Demo

assets/SampleOutput1.png assets/SampleOutput2.png

## 🎯 Goal

To automate accessibility compliance and help developers build inclusive web applications.

---
