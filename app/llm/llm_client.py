import requests
from app.utils.logger import get_logger


class LLMClient:
    def __init__(self, model="mistral", base_url="http://localhost:11434"):
        self.logger = get_logger(__name__)
        self.model = model
        self.base_url = base_url
    
    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()["response"]
        self.logger.info(f"Ollama response: {result[:100]}")
        return result
