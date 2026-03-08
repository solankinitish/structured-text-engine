from app.retrieval.document_loader import DocumentLoader
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_retriever import VectorRetriever

loader = DocumentLoader()
docs = loader.load_documents()

embedding_service = EmbeddingService()

retriever = VectorRetriever(docs, embedding_service)

results = retriever.retrieve("Which language builds APIs?")

print(results)
