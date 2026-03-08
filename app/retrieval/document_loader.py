from pathlib import Path


class DocumentLoader:

    def __init__(self, docs_path="docs"):
        self.docs_path = Path(docs_path)
    
    def load_documents(self):
        documents = []

        for file in self.docs_path.glob("*.txt"):
            with open(file, "r") as f:
                text = f.read()
                chunks = text.split("\n\n")

                documents.extend(chunks)
        
        return documents
