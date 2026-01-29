# backend/rag/retrieval.py

from pathlib import Path
from typing import List, Dict
import json
import numpy as np
from loguru import logger
from sentence_transformers import SentenceTransformer

# -------------------------------
# Directories
# -------------------------------
VECTORSTORE_DIR = Path("./backend/storage/vectorstore")

# -------------------------------
# Model
# -------------------------------
MODEL_NAME = "all-MiniLM-L6-v2"

# -------------------------------
# Caching
# -------------------------------
MODEL = None
ALL_CHUNKS = None

# -------------------------------
# Load embedding model
# -------------------------------
def load_embedding_model():
    logger.info(f"Loading embedding model: {MODEL_NAME}")
    return SentenceTransformer(MODEL_NAME)

def get_model():
    global MODEL
    if MODEL is None:
        MODEL = load_embedding_model()
    return MODEL

# -------------------------------
# Load all embeddings
# -------------------------------
def load_all_embeddings() -> List[Dict]:
    embeddings = []
    vector_files = list(VECTORSTORE_DIR.glob("*.json"))

    logger.info(f"Loading embeddings from {len(vector_files)} files.")

    for vf in vector_files:
        try:
            with open(vf, "r", encoding="utf-8") as f:
                paper_vectors = json.load(f)
                embeddings.extend(paper_vectors)
        except Exception as e:
            logger.error(f"Failed to load {vf.name}: {e}")

    logger.info(f"Loaded {len(embeddings)} total chunks.")
    return embeddings

def get_all_chunks():
    global ALL_CHUNKS
    if ALL_CHUNKS is None:
        ALL_CHUNKS = load_all_embeddings()
    return ALL_CHUNKS

# -------------------------------
# Similarity search
# -------------------------------
def retrieve_similar_chunks(query: str, top_k: int = 5) -> List[Dict]:
    model = get_model()
    all_chunks = get_all_chunks()

    if not all_chunks:
        logger.warning("No embeddings found.")
        return []

    # Encode query
    query_vector = model.encode(query, normalize_embeddings=True)

    # Compute similarity scores
    scores = []
    for chunk in all_chunks:
        vector = np.array(chunk["embedding"])
        score = float(np.dot(query_vector, vector))
        scores.append({
            "paper_id": chunk["paper_id"],
            "chunk_id": chunk["chunk_id"],
            "score": score
        })

    # Return top-k
    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:top_k]

# -------------------------------
# Wrapper for FastAPI
# -------------------------------
def retrieve(query: str, top_k: int = 5):
    """
    FastAPI-friendly function to retrieve top-k similar chunks.
    """
    return retrieve_similar_chunks(query, top_k)

# -------------------------------
# Run as script (debug)
# -------------------------------
if __name__ == "__main__":
    query = "agent architectures for research reasoning"
    results = retrieve(query, top_k=5)

    for r in results:
        print(r)
