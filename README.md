# Smart Document Assistant (RAG)

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions about their contents. The system combines semantic search with a large language model to retrieve relevant context and generate grounded responses.

---

## Overview

Traditional language models rely solely on their pre-trained knowledge and cannot access private or newly uploaded documents. This project implements a Retrieval-Augmented Generation (RAG) pipeline that first retrieves the most relevant information from an uploaded document before generating an answer.

The application performs document ingestion, semantic indexing, vector similarity search, prompt construction, and answer generation through a REST API built with FastAPI.

---

## Features

- Upload PDF documents
- Automatic text extraction
- Semantic chunking
- Dense vector embeddings using SentenceTransformers
- FAISS vector database for similarity search
- Retrieval-Augmented Generation (RAG)
- Google Gemini integration
- FastAPI REST API
- Interactive Swagger documentation

---

## Architecture

```

PDF Upload
↓
Text Extraction
↓
Chunking
↓
Sentence Embeddings
↓
FAISS Vector Index

Question
↓
Question Embedding
↓
Similarity Search
↓
Relevant Chunks
↓
Prompt Engineering
↓
Gemini
↓
Answer

```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| LLM | Google Gemini |
| Embeddings | SentenceTransformers |
| Vector Search | FAISS |
| Document Parsing | PyMuPDF |
| Prompt Engineering | Custom |
| Language | Python |

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/smart-document-assistant.git
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Start the API.

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.

---

## API Endpoints

### Upload Document

```
POST /upload
```

Uploads and indexes a PDF document.

---

### Ask Question

```
POST /ask
```

Example request

```json
{
    "question": "What color is the wallpaper?"
}
```

Example response

```json
{
    "question": "What color is the wallpaper?",
    "answer": "The wallpaper is yellow."
}
```

---

## How It Works

When a document is uploaded, the application extracts the text from the PDF, divides it into semantically meaningful chunks, generates dense vector embeddings, and stores them in a FAISS index.

When the user submits a question, the question is embedded into the same vector space. FAISS retrieves the most semantically similar chunks, which are combined into a prompt and provided to Gemini. The language model then generates an answer using only the retrieved document context.

---

## Future Improvements

- Persistent vector database using Qdrant
- Multi-document support
- Conversation history
- Streaming responses
- React frontend
- Docker deployment
- Authentication
- Cloud deployment

---
