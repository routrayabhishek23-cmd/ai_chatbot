# AI Chatbot using LLMs (Full Stack Project)

A complete full-stack AI chatbot application built with Python, FastAPI, and Streamlit. This project demonstrates clean software architecture, RESTful API design, and integration with modern Large Language Models (LLMs).

## 🚀 Features
- **Modern UI:** Clean, responsive chat interface using Streamlit.
- **Robust Backend:** Fast, asynchronous API built with FastAPI.
- **LLM Integration:** Modular design currently using Google Gemini.
- **Clean Architecture:** Separated concerns between frontend, backend, and core logic.
- **History Management:** Maintains conversation context within the session.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Backend:** FastAPI, Uvicorn, Pydantic
- **Frontend:** Streamlit
- **AI Engine:** Google Gemini (Generative AI)
- **Environment:** python-dotenv

## 📁 Project Structure
```text
ai_chatbot/
├── backend/            # FastAPI source code
│   ├── main.py         # Application entry point
│   └── models.py       # Pydantic data models
├── frontend/           # Streamlit application
│   └── webapp.py       # Chat interface logic
├── core/               # Shared logic
│   └── llm_manager.py  # LLM abstraction layer
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md           # Project documentation
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd ai_chatbot
```

### 2. Set up Environment Variables
Create a `.env` file from the template:
```bash
cp .env.example .env
```
Add your **Google API Key** to the `.env` file. You can get one for free at [Google AI Studio](https://aistudio.google.com/).

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Backend
```bash
python -m backend.main
```
The backend will run at `http://localhost:8000`.

### 5. Run the Frontend (New Terminal)
```bash
streamlit run frontend/webapp.py
```
The UI will open in your browser at `http://localhost:8501`.

## 🧠 Design Decisions
- **Modularity:** The LLM logic is separated into `core/` so switching from Gemini to OpenAI requires minimal changes.
- **Typed Models:** Used Pydantic for strict request/response validation.
- **State Management:** Utilized Streamlit's `session_state` to keep the chat history persistent during the user's session.

## 📄 License
This project is for educational purposes under the MIT License.
