import os
from pathlib import Path
import pdfplumber
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from typing import List
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pdfplumber")

# -------------------------------
# Directories
# -------------------------------
RAW_PAPERS_DIR = Path("./backend/data/papers")
PROCESSED_DIR = Path("./backend/storage/processed")
METADATA_DIR = Path("./backend/storage/metadata")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Metadata model
# -------------------------------
class PaperMetadata(BaseModel):
    title: str
    authors: List[str] = []
    year: str = ""
    venue: str = ""
    file_name: str

# -------------------------------
# PDF Text Extraction
# -------------------------------
def extract_text_from_pdf(file_path: Path) -> str:
    """Extract full text from a PDF using pdfplumber."""
    try:
        with pdfplumber.open(file_path) as pdf:
            # Join text from all pages
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception as e:
        print(f"⚠️ Warning: Failed to extract text from {file_path.name}: {e}")
        return ""

# -------------------------------
# Single paper ingestion
# -------------------------------
def ingest_paper(file_path: Path):
    """Process a single PDF and save text + metadata."""
    print(f"Ingesting {file_path.name}...")

    try:
        text = extract_text_from_pdf(file_path)

        # Save processed text
        processed_file = PROCESSED_DIR / f"{file_path.stem}.txt"
        with open(processed_file, "w", encoding="utf-8") as f:
            f.write(text)

        # Minimal metadata (manual for now, can be extended later)
        metadata = PaperMetadata(
            title=file_path.stem,
            file_name=str(file_path)
        )

        # Save metadata using Pydantic v2
        metadata_file = METADATA_DIR / f"{file_path.stem}.json"
        with open(metadata_file, "w", encoding="utf-8") as f:
            # Use `model_dump_json` instead of deprecated `.json()`
            f.write(metadata.model_dump_json(indent=2, ensure_ascii=False))

        print(f"✅ Ingested {file_path.name}")

    except Exception as e:
        print(f"❌ Failed to ingest {file_path.name}: {e}")

# -------------------------------
# Batch ingestion
# -------------------------------
def ingest_all_papers():
    """Batch ingest all PDFs in the raw papers folder."""
    for file_path in RAW_PAPERS_DIR.glob("*.pdf"):
        ingest_paper(file_path)

# -------------------------------
# Run as script
# -------------------------------
if __name__ == "__main__":
    ingest_all_papers()
