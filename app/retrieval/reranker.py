import numpy as np

class Reranker:

    def __init__(self, embedding_service, threshold=0.5):
        self.embedding_service = embedding_service
        self.threshold = threshold

    def rerank(self, query, documents, top_k=3):

        if not documents:
            return []
        
        query_embedding = self.embedding_service.embed([query])[0]

        texts = [doc["text"] if isinstance(doc, dict) else doc for doc in documents]
        doc_embedding = self.embedding_service.embed(texts)

        scores = np.dot(doc_embedding, query_embedding)
        ranked_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for i in ranked_indices:
            if scores[i] < self.threshold:
                continue

            results.append(documents[i])

            if len(results) == top_k:
                break

        return results
