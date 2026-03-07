from app.services.text_service import TextService
from app.models.schemas import TextRequest, TextResponse
from app.utils.logger import get_logger
from app.llm.llm_client import LLMClient
from app.prompts.prompt_manager import PromptManager
from app.llm.provider_factory import create_provider


class TextController:

    def __init__(self):

        provider = create_provider()
        llm_client = LLMClient(provider)
        prompt_manager = PromptManager()

        self.service = TextService(llm_client, prompt_manager)
        self.logger = get_logger(__name__)
    
    def process_text(self, request: TextRequest) -> TextResponse:

        self.logger.info("Controller received request")

        return self.service.process(request)
