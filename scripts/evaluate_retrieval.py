from app.retrieval.document_loader import DocumentLoader
from app.retrieval.embedding_service import EmbeddingService
from app.retrieval.vector_retriever import VectorRetriever


def evaluate():
    loader = DocumentLoader()
    documents = loader.load_documents()

    embedding_service = EmbeddingService()
    retriever = VectorRetriever(documents, embedding_service)

    test_queries = [
        "What is Python?",
        "What is FastAPI?",
        "What are large language models?",
        "What is the capital of France?"
    ]

    for query in test_queries:
        print("\n=============================")
        print(f"Query: {query}")

        results = retriever.retrieve(query)

        print("Retrieved Context:")

        if not results:
            print("No relevant context found.")
        else:
            for r in results:
                print("-", r["text"])


if __name__ == "__main__":
    evaluate()
