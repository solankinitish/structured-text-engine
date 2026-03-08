from app.config import settings
from app.llm.groq_provider import GroqProvider


def create_provider():
    
    if settings.llm_provider == "groq":
        return GroqProvider()
    
    raise ValueError("Unsupported LLM provider")
