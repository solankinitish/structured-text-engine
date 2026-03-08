class PromptManager:

    def __init__(self):
        self.prompts = {
            "rewrite": "Rewrite the following text professionally:\n\n{text}",
            "summarize": "Summarize the following text:\n\n{text}"
        }

    def get_prompt(self, name: str, text: str) -> str:
        template = self.prompts[name]
        return template.format(text=text)
