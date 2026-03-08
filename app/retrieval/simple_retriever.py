class SimpleRetriever:

    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, query):
        results = []
    
        for doc in self.documents:
            if query.lower() in doc.lower():
                results.append(doc)
            
        return results[:3]
