# StructuredTextEngine

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

StructuredTextEngine is a **Retrieval-Augmented Generation (RAG) backend** built with FastAPI.  
It retrieves relevant knowledge from a vector database and uses that context to generate grounded responses with an LLM.

---

## What This Project Demonstrates

- Building a **RAG pipeline from scratch**
- Using **vector embeddings for semantic retrieval**
- Implementing **retrieval + reranking**
- Designing a **modular LLM backend architecture**
- Integrating **LLMs with FastAPI services**

---

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic document search using embeddings
- Vector database powered retrieval
- Context reranking for better relevance
- Modular LLM provider architecture
- Clean controller → service backend design
- Pipeline logging for observability

---

## Tech Stack

- **FastAPI** — API layer  
- **Sentence Transformers** — embeddings  
- **ChromaDB** — vector database  
- **Groq API** — LLM inference  
- **Python**

---

## Architecture

```
User
 │
 ▼
FastAPI API
 │
 ▼
Controller
 │
 ▼
TextService
 │
 ├─ Retriever
 │   ├─ VectorStore (ChromaDB)
 │   └─ Reranker
 │
 ├─ PromptManager
 │
 └─ LLMClient → Groq
```

---

## RAG Pipeline

```
User Query
     ↓
Embedding Generation
     ↓
Vector Database Search
     ↓
Reranking
     ↓
Context Construction
     ↓
Prompt → LLM
     ↓
Response
```

---

## Example

**Request**

```json
POST /process

{
  "text": "What is Python?"
}
```

**Retrieved Context**

```
Python is a high-level programming language.
FastAPI is a modern web framework for building APIs with Python.
```

**Response**

```
Python is a high-level programming language.
```

---

## Observability

The system logs each stage of the pipeline:

- retrieved documents  
- context used  
- prompt sent to LLM  
- LLM response  

This makes debugging and evaluation of the RAG pipeline easier.

---

## Project Structure

```
app
├── api
├── controllers
├── services
├── retrieval
├── prompts
├── llm
├── utils
└── models
```

---

## Summary

StructuredTextEngine demonstrates a **production-style RAG backend** combining vector retrieval, reranking, prompt orchestration, and LLM inference.
