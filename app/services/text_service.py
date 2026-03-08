from app.utils.logger import get_logger
from app.models.schemas import TextRequest, TextResponse
from app.llm.llm_client import LLMClient
from app.prompts.prompt_manager import PromptManager
from app.exceptions import InvalidInputError


class TextService:

    def __init__(self, llm_client: LLMClient, prompt_manager: PromptManager, retriever):
        self.logger = get_logger(__name__)
        self.llm_client = llm_client
        self.prompt_manager = prompt_manager
        self.retriever = retriever

    def process(self, request: TextRequest) -> TextResponse:

        text = request.text

        # validation
        if not isinstance(text, str):
            raise InvalidInputError("Input must be a string.")
        
        if text.strip() == "":
            raise InvalidInputError("Input text cannot be empty.")
        
        self.logger.info("Processing text with LLM")

        query = request.text

        # retrieve context
        documents = self.retriever.retrieve(query)

        context = "\n".join(documents)

        # build prompt with context
        prompt_input = f"Context:\n{context}\n\nQuestion:\n{query}"

        prompt = self.prompt_manager.get_prompt("rewrite", prompt_input)

        output = self.llm_client.generate(prompt)

        return TextResponse(result=output)
 