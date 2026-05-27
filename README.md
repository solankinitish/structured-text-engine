# StructuredTextEngine

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Ollama](https://img.shields.io/badge/LLM-Ollama%2FMistral-purple)
![RAG](https://img.shields.io/badge/Architecture-RAG-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

StructuredTextEngine is a **fully local Retrieval-Augmented Generation (RAG) backend** built from first principles.
It loads documents from disk, indexes them into a persistent vector store, retrieves semantically relevant context, and generates grounded answers using a local LLM — no internet required.

---

## What This Project Demonstrates

- Building a **RAG pipeline from scratch** with clean modular architecture
- **Persistent vector storage** using ChromaDB across sessions
- **Semantic retrieval + cosine similarity reranking** for better relevance
- **Modular LLM provider design** — swap providers without touching business logic
- **Dependency injection via Container** — clean separation of concerns
- **Grounding enforcement** — answers only from retrieved context

---

## Features

- **Fully local pipeline** — no API keys, no internet, runs entirely on-device
- **Persistent ChromaDB** — documents indexed once, retrieved across sessions
- **Semantic search** — SentenceTransformers embeddings for dense retrieval
- **Cosine similarity reranking** — retrieved docs rescored against query before answering
- **Grounding enforcement** — LLM answers only from retrieved context; returns "I don't know" otherwise
- **Modular architecture** — Container wires all dependencies; each layer independently testable
- **Full pipeline logging** — every stage logged for systematic debugging

---

## Tech Stack

| Component | Technology |
|---|---|
| API | FastAPI, Uvicorn |
| LLM | Ollama (Mistral local) |
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| Vector Store | ChromaDB (persistent) |
| Reranking | Cosine similarity (numpy) |
| Language | Python 3.11 |

---

## Architecture

```
User Query (POST /process)
│
▼
FastAPI → Router → Controller
│
▼
TextService
├── VectorRetriever
│   ├── EmbeddingService → query embedding
│   ├── VectorStore (ChromaDB) → top-10 recall
│   └── Reranker → cosine similarity → top-3
├── PromptManager → build grounded prompt
└── LLMClient → Ollama/Mistral → answer
│
▼
TextResponse
```

---

## RAG Pipeline

```
Documents (docs/*.txt)
↓
DocumentLoader → chunks
↓
EmbeddingService → dense vectors
↓
ChromaDB (persistent storage)

Query
↓
EmbeddingService → query vector
↓
ChromaDB → top-10 recall
↓
Reranker → cosine similarity → top-3
↓
PromptManager → grounded prompt
↓
LLMClient → Ollama/Mistral
↓
Grounded Answer
```

---

## Example

**Request**
```json
POST /process
{
  "text": "What are embeddings?"
}
```

**Retrieved Context**
```
Embeddings are numerical representations of text that capture semantic meaning.
Sentence Transformers are used to generate dense vector embeddings for semantic search.
Vector search finds semantically similar documents using cosine similarity.
```

**Response**
```
Embeddings are numerical representations of text that capture semantic meaning.
```

---

## Evaluation

5 queries tested against the local pipeline:

| Query | Type | Result |
|---|---|---|
| What is Python? | factual | PASS ✅ |
| What is RAG? | acronym query | PARTIAL ⚠️ |
| What are embeddings? | conceptual | PASS ✅ |
| What is the capital of France? | grounding test | PASS ✅ |
| Who created FastAPI? | grounding test | PASS ✅ |

**Score: 4/5**

---

## How to Run

**1. Clone and install dependencies**
```bash
git clone https://github.com/solankinitish/structured-text-engine
cd structured-text-engine
pip install -r requirements.txt
```

**2. Install Ollama and pull Mistral**
```bash
ollama pull mistral
```

**3. Start the API server**
```bash
uvicorn app.api.server:app --reload
```

**4. Run the evaluation**
```bash
python -m scripts.evaluate
```

**5. Test manually**
```bash
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{"text": "What are embeddings?"}'
```

---

## Project Structure

```
structured-text-engine/
├── app/
│   ├── api/
│   │   ├── server.py           — FastAPI app, middleware
│   │   ├── routes.py           — API endpoints
│   │   ├── middleware.py       — request logging
│   │   └── error_handlers.py  — exception handling
│   ├── core/
│   │   └── container.py        — dependency injection
│   ├── llm/
│   │   └── llm_client.py       — Ollama LLM wrapper
│   ├── retrieval/
│   │   ├── document_loader.py  — loads .txt files from docs/
│   │   ├── embedding_service.py — SentenceTransformers embeddings
│   │   ├── vector_store.py     — ChromaDB persistent store
│   │   ├── vector_retriever.py — semantic retrieval + reranking
│   │   └── reranker.py         — cosine similarity reranker
│   ├── prompts/
│   │   └── prompt_manager.py   — prompt templates
│   ├── services/
│   │   └── text_service.py     — orchestrates RAG pipeline
│   ├── models/
│   │   └── schemas.py          — Pydantic request/response models
│   └── utils/
│       └── logger.py           — logging
├── docs/
│   └── knowledge.txt           — document knowledge base
├── scripts/
│   └── evaluate.py             — evaluation benchmark
├── data/
│   └── vector_db/              — ChromaDB persistent storage
├── requirements.txt
└── .gitignore
```

---

## Known Limitations

- **Acronym sensitivity** — queries using acronyms (e.g. "RAG") may fail to retrieve documents where the full term is used; query expansion would address this
- **Static knowledge base** — documents loaded once at startup; adding new docs requires restart
- **Single file ingestion** — DocumentLoader reads .txt files only; PDF/HTML not supported
- **Paragraph chunking** — splits on double newline; no overlap, no semantic chunking
- **Local LLM latency** — Ollama/Mistral averages 10-40s per query
- **No authentication** — API is open, no rate limiting

---

## Summary

StructuredTextEngine demonstrates a **fully local production-style RAG backend** combining persistent vector storage, semantic retrieval, cosine similarity reranking, modular dependency injection, and local LLM inference — built and understood from first principles.