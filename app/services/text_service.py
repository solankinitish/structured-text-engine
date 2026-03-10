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

        self.logger.info(f"Retrieved documents: {documents}")

        if not documents or len(documents) == 0:
            return TextResponse(result="I don't know based on the available context.")

        context = "\n".join(doc["text"] for doc in documents)

        self.logger.info(f"Context used:\n{context}")

        # build prompt with context
        prompt_input = f"{context}\n\nQuestion:\n{query}"

        prompt = self.prompt_manager.get_prompt("qa", prompt_input)

        self.logger.info(f"Prompt sent to LLM:\n{prompt}")

        output = self.llm_client.generate(prompt)

        self.logger.info(f"LLM response: {output}")

        return TextResponse(result=output)
 