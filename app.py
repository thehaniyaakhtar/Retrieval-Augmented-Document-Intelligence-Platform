from pdf_processor import extract_text
from chunker import create_chunks
from embedder import create_embeddings
from vector_store import create_index, search_index
from rag import build_prompt
from llm import generate_answer

text = extract_text("sample.pdf")
chunks = create_chunks(text)
embeddings = create_embeddings(chunks)
index = create_index(embeddings)

question = "What color is the wallpaper"
question_embedding = create_embeddings([question])[0]
indices = search_index(index, question_embedding)

# print(f"Number of chunks: {len(chunks)}")
# print(f"Embeddings: {len(embeddings)}")
# print(f"Embedding dimensions: {len(embeddings[0])}")

# print("Retrieved Chunks:\n")

# for idx in indices:
#     print("-"*50)
#     print(chunks[idx])
retrieved_chunks = [chunks[idx] for idx in indices]
prompt = build_prompt(question, retrieved_chunks)
answer = generate_answer(prompt)
print(answer)
answer = generate_answer(prompt)

print("\nAnswer:\n")
print(answer)