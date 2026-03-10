class PromptManager:

    def __init__(self):
        self.prompts = {
            "qa": """
You are a helpful assistant.

Answer the question using ONLY the provided context.

If the answer is not present in the context, say "I don't know".

Context:
{text}

Answer:
"""
        }

    def get_prompt(self, name: str, text: str) -> str:
        template = self.prompts[name]
        return template.replace("{text}", text)
