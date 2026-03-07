class LLMClient:

    def __init__(self, provider):
        self.provider = provider
    
    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
