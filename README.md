# PromptCraft AI ✦

> Transform weak prompts into powerful ones instantly using AI

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Groq](https://img.shields.io/badge/Groq-Llama3.1-green)
![IBM](https://img.shields.io/badge/IBM-SkillsBuild-052FAD)
![License](https://img.shields.io/badge/License-MIT-yellow)

---
## 🖥️ Screenshot
![PromptCraft AI](Screenshot%202026-04-07%20101527.png)
![PromptCraft AI](Screenshot%202026-04-07%20101633.png)



## 🌐 Live Demo
👉 **[Try it here](https://promptcraft-ai-kgwbjnn4t8iuq2oztfvi6m.streamlit.app)**

---

## 📌 About
PromptCraft AI is an AI-powered prompt improver 
built as a practical project after completing the 
IBM SkillsBuild "Craft Precise Prompts for AI Models" 
certification.

It takes your rough, vague prompt and transforms it 
into a clear, precise and powerful one — instantly!

---

## ✨ Features
- Takes any rough prompt as input
- Improves clarity, structure and precision
- Explains what changed and why
- Guides anyone with simple 3 step instructions
- Supports 6 prompt types:
  - General
  - Creative
  - Technical
  - Formal
  - Academic
  - Marketing

---

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app framework |
| Groq API | AI inference engine |
| Llama 3.1 | Language model |

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/MinnaNourin/PromptCraft-AI.git
cd PromptCraft-AI
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Get your free Groq API key**
```
Go to → https://console.groq.com/keys
Sign up free → Create API Key → Copy it
```

**Step 4 — Create secrets file**
```
Create .streamlit/secrets.toml and add:
GROQ_API_KEY = "your_groq_key_here"
```

**Step 5 — Run the app**
```bash
streamlit run app.py
```

---

## 📁 Project Structure
```
PromptCraft-AI/
├── .streamlit/
│   └── secrets.toml    ← API key (not pushed)
├── .gitignore
├── app.py              ← Main application
├── requirements.txt    ← Dependencies
└── README.md           ← You are here
```

---

## 💡 How to Use
```
1. Enter your rough prompt
2. Select the prompt type
3. Click ✦ Craft My Prompt
4. Copy the improved prompt
5. Paste into ChatGPT, Gemini or Claude
6. Get a much better response!
```

---

## 🏅 Certification
This project was built as a practical application 
of the IBM SkillsBuild certification:

**Craft Precise Prompts for AI Models**
- Issued by: IBM SkillsBuild
- Issued on: 05 April 2026
- Verify: https://www.credly.com/go/fL6rkCD3

---

## 👩‍💻 Built by
**Minna Nourin**
IBM SkillsBuild Certified — Prompt Engineering

---

## 📄 License
This project is open source and available 
under the MIT License.
