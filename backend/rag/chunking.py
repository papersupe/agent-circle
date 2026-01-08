# backend/rag/chunking.py

from pathlib import Path
from typing import List, Dict
from loguru import logger
import json

# -------------------------------
# Directories
# -------------------------------
PROCESSED_DIR = Path("./backend/storage/processed")
CHUNKS_DIR = Path("./backend/storage/chunks")

CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Chunking config
# -------------------------------
MAX_CHARS_PER_CHUNK = 1500
MIN_CHARS_PER_CHUNK = 300

# -------------------------------
# Chunk model (simple dict for now)
# -------------------------------
def make_chunk(
    paper_id: str,
    chunk_id: int,
    text: str
) -> Dict:
    return {
        "paper_id": paper_id,
        "chunk_id": chunk_id,
        "text": text.strip(),
        "char_length": len(text)
    }

# -------------------------------
# Core chunking logic
# -------------------------------
def chunk_text(text: str, paper_id: str) -> List[Dict]:
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = []

    current_buffer = ""
    chunk_id = 0

    for para in paragraphs:
        if len(current_buffer) + len(para) <= MAX_CHARS_PER_CHUNK:
            current_buffer += para + "\n"
        else:
            if len(current_buffer) >= MIN_CHARS_PER_CHUNK:
                chunks.append(make_chunk(paper_id, chunk_id, current_buffer))
                chunk_id += 1
                current_buffer = para + "\n"
            else:
                # Force-append if buffer too small
                current_buffer += para + "\n"

    if current_buffer.strip():
        chunks.append(make_chunk(paper_id, chunk_id, current_buffer))

    return chunks

# -------------------------------
# Chunk a single processed paper
# -------------------------------
def chunk_paper(processed_file: Path):
    paper_id = processed_file.stem
    logger.info(f"Chunking paper: {paper_id}")

    try:
        text = processed_file.read_text(encoding="utf-8", errors="ignore")

        if not text.strip():
            logger.warning(f"No text found for {paper_id}, skipping chunking.")
            return []

        chunks = chunk_text(text, paper_id)

        output_file = CHUNKS_DIR / f"{paper_id}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

        logger.success(f"Created {len(chunks)} chunks for {paper_id}")
        return chunks

    except Exception as e:
        logger.error(f"Failed to chunk {paper_id}: {e}")
        return []

# -------------------------------
# Batch chunking
# -------------------------------
def chunk_all_papers():
    processed_files = list(PROCESSED_DIR.glob("*.txt"))
    logger.info(f"Found {len(processed_files)} processed papers to chunk.")

    for file_path in processed_files:
        chunk_paper(file_path)

# -------------------------------
# Run as script
# -------------------------------
if __name__ == "__main__":
    chunk_all_papers()
