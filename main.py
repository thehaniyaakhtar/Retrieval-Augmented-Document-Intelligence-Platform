from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from pdf_processor import extract_text
from chunker import create_chunks
from embedder import create_embeddings
from vector_store import create_index, search_index
from prompt_builder import build_prompt
from llm import generate_answer

app = FastAPI()

# Store the current document in memory
index = None
chunks = None


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Smart Document Assistant API"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global index
    global chunks

    # Save uploaded PDF
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    # Process document
    text = extract_text(file.filename)

    chunks = create_chunks(text)

    embeddings = create_embeddings(chunks)

    index = create_index(embeddings)

    return {
        "message": "Document processed successfully",
        "chunks": len(chunks)
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    global index
    global chunks

    if index is None:
        return {
            "error": "Please upload a document first."
        }

    question = request.question

    # Embed the question
    question_embedding = create_embeddings([question])[0]

    # Retrieve most relevant chunks
    indices = search_index(index, question_embedding, k=5)

    retrieved_chunks = []
    
    print("\nRetrieved Chunks:\n")
    
    for idx in indices:
        print("-" * 70)
        print(chunks[idx])
        retrieved_chunks.append(chunks[idx])
        

    # Build prompt
    prompt = build_prompt(
        question,
        retrieved_chunks
    )

    # Ask Gemini
    print("\nPrompt sent to Gemini:\n")
    print(prompt)
    
    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer
    }