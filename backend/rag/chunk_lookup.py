from pathlib import Path
from typing import List, Dict
import json
from loguru import logger

# -------------------------------
# Directories
# -------------------------------
CHUNKS_DIR = Path("./backend/storage/chunks")

# -------------------------------
# Load chunks for a paper
# -------------------------------
def load_chunks_for_paper(paper_id: str) -> List[Dict]:
    chunk_file = CHUNKS_DIR / f"{paper_id}.json"

    if not chunk_file.exists():
        logger.warning(f"Chunk file not found for paper: {paper_id}")
        return []

    try:
        with open(chunk_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load chunks for {paper_id}: {e}")
        return []

# -------------------------------
# Lookup chunk texts
# -------------------------------
def lookup_chunks(
    retrieval_results: List[Dict]
) -> List[Dict]:
    """
    retrieval_results format:
    [
        {"paper_id": str, "chunk_id": int, "score": float},
        ...
    ]
    """
    resolved = []
    cache = {}

    for item in retrieval_results:
        paper_id = item["paper_id"]
        chunk_id = item["chunk_id"]
        score = item["score"]

        if paper_id not in cache:
            cache[paper_id] = load_chunks_for_paper(paper_id)

        chunks = cache[paper_id]
        match = next(
            (c for c in chunks if c["chunk_id"] == chunk_id),
            None
        )

        if match:
            resolved.append({
                "paper_id": paper_id,
                "chunk_id": chunk_id,
                "score": score,
                "text": match["text"],
                "char_length": match["char_length"]
            })
        else:
            logger.warning(
                f"Chunk {chunk_id} not found in paper {paper_id}"
            )

    return resolved

# -------------------------------
# Debug run
# -------------------------------
if __name__ == "__main__":
    # Example manual test
    example_results = [
        {"paper_id": "Agent0", "chunk_id": 2, "score": 0.48}
    ]

    resolved = lookup_chunks(example_results)
    for r in resolved:
        print("-" * 80)
        print(f"[{r['paper_id']} | chunk {r['chunk_id']} | score {r['score']:.3f}]")
        print(r["text"][:500])
