import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for a better look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stChatFloatingInputContainer {
        bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Personal AI Assistant")
st.markdown("---")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Sidebar info
with st.sidebar:
    st.title("Project Info")
    st.info("""
    **Core Technologies:**
    - FastAPI (Backend)
    - Streamlit (Frontend)
    - Google Gemini (LLM)
    
    **Developed by:**
    Abhishek Routray
    """)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Call Backend API
        with st.spinner("AI is thinking..."):
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={"message": prompt},
                timeout=30
            )
            
            if response.status_code == 200:
                ai_reply = response.json().get("response")
                # Display assistant response
                with st.chat_message("assistant"):
                    st.markdown(ai_reply)
                # Add assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend. Is FastAPI running?")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
