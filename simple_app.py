import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
st.set_page_config(page_title="Simple AI Chat", page_icon="🚀")

# 2. Configure AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Please add your GOOGLE_API_KEY in the .env file!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-flash-latest')

# 3. UI Design
st.title("🚀 Quick AI Assistant - by Abhishek Routray")
st.caption("A simple, one-file version of the Full-Stack Chatbot")

# 4. Chat logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"AI Error: {e}")
