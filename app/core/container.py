from app.llm.llm_client import LLMClient
from app.prompts.prompt_manager import PromptManager

from app.retrieval.document_loader import DocumentLoader
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_retriever import VectorRetriever

from app.services.text_service import TextService


class Container:

    def __init__(self):

        loader = DocumentLoader()
        documents = loader.load_documents()

        embedding_service = EmbeddingService()

        retriever = VectorRetriever(documents, embedding_service)

        llm_client = LLMClient()

        prompt_manager = PromptManager()

        self.text_service = TextService(
            llm_client=llm_client,
            prompt_manager=prompt_manager,
            retriever=retriever
        )
