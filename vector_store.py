import faiss
import numpy as np

def create_index(embeddings):
    dimension = len(embeddings[0])
    
    index = faiss.IndexFlatL2(dimension)
    
    embeddings = np.array(embeddings).astype("float32")
    
    index.add(embeddings)
    
    return index

def search_index(index, question_embedding, k=5):
    question_embedding = np.array([question_embedding]).astype("float32")
    distances, indices = index.search(question_embedding, k)
    
    return indices[0]