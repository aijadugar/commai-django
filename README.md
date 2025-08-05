# 🧠 CommAI – Communication Skill Analyzer (Django + NLP)

**CommAI** is an AI-powered web application that evaluates a user’s **communication skills** through both **text and speech inputs**, using **Natural Language Processing (NLP)** and a **Django-based backend**. The system analyzes a user’s response across multiple communication parameters and provides detailed, real-time feedback to help improve their communication effectiveness.

> 🔥 The project that blends AI, NLP, speech processing, and real-time feedback into a single intelligent platform.

---

## 📌 Features

- 💬 **Text Interface**: Users can type messages to receive parameter-based feedback.
- 🎙️ **Speech Interface**: Users can record audio; the app converts it to text and analyzes it.
- 🧠 **Seven NLP Parameters Analyzed**:
  - Clarity
  - Conciseness
  - Tone & Sentiment
  - Engagement
  - Grammar & Spelling
  - Vocabulary Usage
  - Persuasiveness
- 🧾 **Auto-generated feedback** and level assessment: *Poor*, *Intermediate*, *Excellent*
- 🧊 **Ollama integration** for large language model-based evaluation (optional)
- 🖼️ Dynamic UI with JS interactivity + auto-disabling select tags
- 📦 Modular, scalable Django structure

---

## 🛠️ Tech Stack

| Component           | Technology Used        |
|--------------------|------------------------|
| Frontend           | HTML5, CSS3, Bootstrap, JavaScript |
| Backend            | Django (Python)        |
| Speech Recognition | `speech_recognition`, `pyaudio` |
| NLP Processing     | Python NLP libraries, Gemini API OpenAI whisper |
| Database           | SQLite (Django default) |
| File Handling      | Django static & media routing |

---

## 
📂 Project Structure

commai-django-Yash/
├── commapp/
│ ├── static/
│ ├── templates/
│ ├── views.py
│ ├── urls.py
│ └── ...
├── commai/
│ ├── settings.py
│ └── urls.py
├── media/
├── db.sqlite3
├── manage.py
└── README.md


---

## 🚀 How to Run the Project

### ✅ Prerequisites

- Python 3.8+
- pip
- Git
- OpenAI Whisper (for speech to text conversion)
- Gemini API

### 📦 Install Required Packages
pip install -r requirements.txt

⚙️ Run the App Locally
git clone https://github.com/YashKerkarTech04/commai-django-Yash.git
cd commai-django-Yash
python manage.py migrate
python manage.py runserver

🧪 Usage Guide
💬 Text Evaluation
Type your answer in the chat box
Click Send
Wait for backend to return parameter-wise analysis and level

🎤 Speech Evaluation
Record your answer via microphone
System converts to text and evaluates it similarly
Results shown below the chat window

🌱 Future Enhancements
User login and progress tracking
Leaderboard for gamified skill improvement
Multilingual support (Hindi, Marathi, etc.)
Deployment to cloud (Render, Vercel, etc.)
API-based analysis engine (Flask or FastAPI microservice)
```bash
pip install -r requirements.txt
