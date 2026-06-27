def build_prompt(question, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a helpful assistant.

Answer the user's question using ONLY the provided context.

If the answer is not present in the context, say:
"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt