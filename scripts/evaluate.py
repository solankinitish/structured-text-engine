import requests

BASE_URL = "http://localhost:8000"

queries = [
    {
        "query": "What is Python?",
        "expected": "Python is a high-level programming language.",
        "answerable": True
    },
    {
        "query": "What is RAG?",
        "expected": "RAG combines retrieval and generation to produce grounded answers.",
        "answerable": True
    },
    {
        "query": "What are embeddings?",
        "expected": "Embeddings are numerical representations of text that capture semantic meaning.",
        "answerable": True
    },
    {
        "query": "What is the capital of France?",
        "expected": "I don't know",
        "answerable": False
    },
    {
        "query": "Who created FastAPI?",
        "expected": "I don't know",
        "answerable": False
    }
]

if __name__ == "__main__":
    print("\n=== StructuredTextEngine Evaluation ===\n")
    passed = 0

    for item in queries:
        try:
            response = requests.post(
                f"{BASE_URL}/process",
                json={"text": item["query"]},
                timeout=60
            )
            actual = response.json().get("result", "").strip()
            print(f"Query: {item['query']}")
            print(f"Expected: {item['expected']}")
            print(f"Actual: {actual}")
            print("---")
            passed += 1
        except Exception as e:
            print(f"❌ {item['query']} ERROR: {e}")

    print(f"\nCompleted: {passed}/{len(queries)} queries")
