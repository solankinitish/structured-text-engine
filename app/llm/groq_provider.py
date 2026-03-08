from app.llm.base_provider import BaseLLMProvider

class GroqProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> str:
        response = f"Groq response: {prompt.upper()}"

        return response
