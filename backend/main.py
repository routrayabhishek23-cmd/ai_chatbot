import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Add the project root to sys.path so we can import from 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.models import ChatRequest, ChatResponse
from core.llm_manager import LLMManager

app = FastAPI(title="AI Chatbot Backend", description="FastAPI service for LLM Interaction")

# Enable CORS so Streamlit can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the AI Logic
llm = LLMManager()

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main endpoint to process chat messages.
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    # Logic to get response from LLM
    ai_response = llm.get_response(request.message)
    
    if ai_response.startswith("Error"):
        raise HTTPException(status_code=500, detail=ai_response)
        
    return ChatResponse(response=ai_response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
