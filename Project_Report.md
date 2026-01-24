# PROJECT REPORT: DESIGN AND IMPLEMENTATION OF AN AI CHATBOT USING LLMs

**Submitted by:** Abhishek Routray

## 1. ABSTRACT
This project presents the development of a full-stack AI chatbot application designed to provide interactive conversational experiences using Large Language Models (LLMs). By leveraging FastAPI for the backend and Streamlit for the frontend, the system demonstrates a robust architecture that separates concerns between user interface, logic processing, and external AI integration. The primary contribution of this work is a modular framework that allows for seamless integration of various LLM providers (e.g., Google Gemini, OpenAI) while maintaining high performance and code readability.

## 2. INTRODUCTION
In the era of Generative AI, chatbots have evolved from simple rule-based systems to sophisticated intelligent agents. This project aims to bridge the gap between complex AI models and end-users by creating a user-friendly web interface. We utilize Python as the primary programming language due to its extensive ecosystem for both web development and AI.

## 3. SYSTEM ARCHITECTURE
The system follows a three-tier architecture:

1.  **Presentation Tier:** Built with Streamlit, providing a chat interface that handles user input and displays AI-generated responses.
2.  **Application Tier:** Built with FastAPI, acting as a REST API that processes requests, validates data using Pydantic, and communicates with the AI module.
3.  **Service Tier (AI Engine):** An abstraction layer that interacts with the Google Gemini API to process prompts and generate natural language responses.

### Data Flow Diagram (Description)
User Input (Streamlit) -> HTTP POST Request (JSON) -> FastAPI endpoint (`/chat`) -> LLM Manager -> Google Gemini API -> LLM Manager -> FastAPI Response -> Streamlit UI Display.

## 4. TECHNOLOGY STACK
- **Python:** The core language for development.
- **FastAPI:** A modern, high-performance web framework for building APIs. Chosen for its speed and automatic documentation (Swagger).
- **Streamlit:** An open-source Python library used for creating custom web apps for data science and machine learning.
- **Pydantic:** Used for data validation and settings management using Python type annotations.
- **Google Gemini API:** The underlying Large Language Model used for natural language processing.
- **Dotenv:** For secure configuration management.

## 5. DESIGN DECISIONS
- **Loose Coupling:** By implementing an `LLMManager` class, the application is not tied to a specific AI provider. This ensures future scalability.
- **CORS Handling:** Implemented Cross-Origin Resource Sharing (CORS) middleware in FastAPI to allow safe communication with the Streamlit frontend.
- **Session State:** Streamlit’s session state is used to store message history locally, ensuring a consistent user experience during the session without needing a persistent database for this prototype.

## 6. WORKFLOW OF THE CHATBOT
1.  **Initialization:** The backend initializes the LLM connection using the provided API key.
2.  **Input Capture:** The user types a message in the Streamlit interface.
3.  **API Call:** Streamlit sends a JSON payload `{"message": "..."}` to the FastAPI `/chat` endpoint.
4.  **Processing:** FastAPI validates the input and calls the Gemini API via the `core` logic.
5.  **Output:** The generated text is returned to the frontend and rendered in the chat bubble.

## 7. SCREENSHOTS (PLACEHOLDERS)
*(In your actual report, insert images of:)*
1.  The Streamlit UI with a sample chat.
2.  The FastAPI Swagger UI (`http://localhost:8000/docs`).
3.  The terminal showing the backend and frontend logs.

## 8. FUTURE SCOPE
- **Integration of Vector Databases:** To implement Retrieval-Augmented Generation (RAG) for company-specific knowledge.
- **Multi-modal Support:** Adding the ability to upload images/PDFs for the AI to analyze.
- **User Authentication:** Implementing OAuth2 or JWT for secure user login.
- **Database Integration:** Using PostgreSQL or MongoDB to store chat history permanently.

## 9. CONCLUSION
This project successfully demonstrates the implementation of a modern AI application. The use of FastAPI and Streamlit proved to be highly efficient for rapid prototyping. The modular design ensures that the system is maintainable and ready for future enhancements in the rapidly evolving field of AI.
