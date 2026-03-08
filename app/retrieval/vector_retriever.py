import numpy as np


class VectorRetriever:

    def __init__(self, documents, embedding_service):
        self.documents = documents
        self.embedding_service = embedding_service

        self.doc_embeddings = embedding_service.embed(documents)
    
    def retrieve(self, query, top_k=3):
        query_embedding = self.embedding_service.embed([query])[0]

        scores = np.dot(self.doc_embeddings, query_embedding)

        top_indices = np.argsort(scores)[::-1][:top_k]

        return [self.documents[i] for i in top_indices]
