from app.utils.logger import get_logger
from app.models.schemas import TextRequest, TextResponse
from app.llm.llm_client import LLMClient
from app.prompts.prompt_manager import PromptManager


class TextService:

    def __init__(self, llm_client: LLMClient, prompt_manager: PromptManager):
        self.logger = get_logger(__name__)
        self.llm_client = llm_client
        self.prompt_manager = prompt_manager

    def process(self, request: TextRequest) -> TextResponse:
        
        self.logger.info("Processing text with LLM")

        prompt = self.prompt_manager.get_prompt("rewrite", request.text)

        output = self.llm_client.generate(prompt)

        return TextResponse(result=output)
 