# 🤖 GenReply

A Windows-based Python automation project that combines **PyAutoGUI**, **clipboard automation**, and the **Google Gemini API** to automatically read chat messages, generate AI-powered replies, and send them.

## ✨ Features

* 🤖 Gemini-powered response generation
* 🖥️ Windows desktop automation
* 🖱️ Mouse and keyboard automation with PyAutoGUI
* 📋 Clipboard-based chat extraction
* 💬 Automatic message detection
* 🌐 English, Hindi, and Odia response support
* 🔄 Continuous chat monitoring
* 📐 Dynamic screen-resolution detection

## 🛠️ Tech Stack

* **Python**
* **Google GenAI SDK**
* **Gemini API**
* **PyAutoGUI**
* **Pyperclip**
* **Windows User32 API**

## ⚙️ How It Works

```text
Chat Window
     ↓
Select & Copy Chat
     ↓
Read Clipboard
     ↓
Detect New Message
     ↓
Gemini API
     ↓
Generate Reply
     ↓
Paste & Send
```

The application continuously monitors the configured chat window. When a new message from the specified sender is detected, the conversation history is sent to Gemini, which generates a short conversational response.

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

python -m venv .venv
.venv\Scripts\activate

pip install google-genai pyautogui pyperclip
```

## 🔐 API Key

**Never commit your real API key to GitHub.**

Use an environment variable instead:

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)
```

Add `.env`, virtual environments, and Python cache files to `.gitignore`.

## 🖱️ Screen Coordinates

The automation currently uses fixed screen coordinates for clicking, selecting chat history, and entering messages.

If your screen resolution or application layout is different, these coordinates may need to be updated.

You can find your mouse coordinates with:

```python
import pyautogui

while True:
    print(pyautogui.position())
```

## ⚠️ Limitations

Because this project relies on screen coordinates, it may be affected by:

* Different screen resolutions
* Display scaling
* Window positions
* Changes to the chat application's UI

For more reliable production automation, an official API or accessibility/DOM-based approach is preferable where available.

## 🔒 Responsible Use

Use this project responsibly and comply with the terms and automation policies of the chat platform you interact with.

Do not commit API keys, passwords, cookies, tokens, private conversations, or other sensitive information.

## 📌 Project Status

**Experimental / Personal Automation**

Built as a practical project demonstrating the integration of **Python + Desktop Automation + Gemini AI**.
