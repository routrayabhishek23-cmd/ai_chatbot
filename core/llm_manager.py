import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class LLMManager:
    """
    Handles communication with different LLM providers.
    Currently supports Google Gemini.
    """
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "GEMINI").upper()
        self._setup_gemini()

    def _setup_gemini(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("Warning: GOOGLE_API_KEY not found in environment.")
            return
        genai.configure(api_key=api_key)
        # Using gemini-flash-latest which has better free tier quota limits
        self.model = genai.GenerativeModel('gemini-flash-latest')

    def get_response(self, prompt: str) -> str:
        """
        Sends a prompt to the configured LLM and returns the text response.
        """
        try:
            if self.provider == "GEMINI":
                response = self.model.generate_content(prompt)
                return response.text
            else:
                return "Error: Unsupported LLM Provider."
        except Exception as e:
            return f"Error connecting to AI Provider: {str(e)}"
