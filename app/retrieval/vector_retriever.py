from app.retrieval.vector_store import VectorStore
from app.retrieval.reranker import Reranker


class VectorRetriever:

    def __init__(self, documents, embedding_service):
        self.embedding_service = embedding_service
        self.vector_store = VectorStore()
        self.reranker = Reranker(embedding_service)

        chunks = []

        for i, doc in enumerate(documents):
            chunks.append({
                "text": doc,
                "metadata": {"chunk_id": i}
            })

        embeddings = embedding_service.embed(documents)

        self.vector_store.add_documents(chunks, embeddings)
    
    def retrieve(self, query, top_k=3):
        query_embedding = self.embedding_service.embed([query])[0]

        docs = self.vector_store.search(query_embedding, k=10)

        texts = [doc["text"] for doc in docs]

        reranked = self.reranker.rerank(query, docs, top_k)

        return reranked
