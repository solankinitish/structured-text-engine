# StructuredTextEngine

StructuredTextEngine is a Retrieval-Augmented Generation (RAG) backend built with FastAPI.

## Features

- Semantic document retrieval using sentence embeddings
- Retrieval Augmented Generation (RAG)
- Modular LLM provider architecture
- Prompt management layer
- Clean service / controller backend architecture

## Tech Stack

- FastAPI
- Sentence Transformers
- Groq LLM API
- Python

## Architecture

User Query
-> Retriever
-> Context Construction
-> Prompt Builder
-> LLM Generation
-> Response
