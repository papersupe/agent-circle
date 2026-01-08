from pathlib import Path
from typing import List, Dict
from loguru import logger
import json

from sentence_transformers import SentenceTransformer

# -------------------------------
# Directories
# -------------------------------
CHUNKS_DIR = Path("./backend/storage/chunks")
VECTORSTORE_DIR = Path("./backend/storage/vectorstore")

VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Embedding model
# -------------------------------
MODEL_NAME = "all-MiniLM-L6-v2"

def load_embedding_model():
    logger.info(f"Loading embedding model: {MODEL_NAME}")
    return SentenceTransformer(MODEL_NAME)

# -------------------------------
# Embed a single chunk file
# -------------------------------
def embed_chunk_file(
    chunk_file: Path,
    model: SentenceTransformer
) -> List[Dict]:
    paper_id = chunk_file.stem
    logger.info(f"Embedding chunks for paper: {paper_id}")

    try:
        with open(chunk_file, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        texts = [chunk["text"] for chunk in chunks]
        embeddings = model.encode(
            texts,
            show_progress_bar=False,
            normalize_embeddings=True
        )

        embedded_chunks = []
        for chunk, vector in zip(chunks, embeddings):
            embedded_chunks.append({
                "paper_id": chunk["paper_id"],
                "chunk_id": chunk["chunk_id"],
                "embedding": vector.tolist(),
                "char_length": chunk["char_length"]
            })

        output_file = VECTORSTORE_DIR / f"{paper_id}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(embedded_chunks, f, indent=2)

        logger.success(
            f"Embedded {len(embedded_chunks)} chunks for {paper_id}"
        )
        return embedded_chunks

    except Exception as e:
        logger.error(f"Failed to embed {paper_id}: {e}")
        return []

# -------------------------------
# Batch embedding
# -------------------------------
def embed_all_chunks():
    chunk_files = list(CHUNKS_DIR.glob("*.json"))
    logger.info(f"Found {len(chunk_files)} chunk files to embed.")

    model = load_embedding_model()

    for chunk_file in chunk_files:
        embed_chunk_file(chunk_file, model)

# -------------------------------
# Run as script
# -------------------------------
if __name__ == "__main__":
    embed_all_chunks()
