from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    """Schema for the incoming chat request."""
    message: str

class ChatResponse(BaseModel):
    """Schema for the outgoing chat response."""
    response: str
    status: str = "success"

class ErrorResponse(BaseModel):
    """Schema for error messages."""
    detail: str
