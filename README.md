# Agent Circle

**Agent Circle** is PaperSupe’s experimental research intelligence system: a **single-agent AI** designed to ingest academic papers, extract concepts, and reason over knowledge in a structured, agentic way.
Currently, it operates in **Reading-Only mode**, focusing on research ingestion, concept extraction, and linking.

---

## Features

* **PDF Ingestion** – Extract text from research papers and store structured metadata.
* **Metadata Management** – Store paper metadata including title, authors, venue, and year.
* **Concept Extraction (Experimental)** – Identify key ideas and concepts from papers.
* **Status API** – Expose agent status and capabilities via FastAPI endpoints.
* **FastAPI Backend** – Versioned, modular API structure for future expansion.
* **Logging** – Structured logs with `loguru` for monitoring ingestion and system events.
* **Pydantic v2 Ready** – Modern, type-safe data validation and JSON serialization.

---

## Project Structure

```
agent-circle/
├── backend/
│   ├── api/
│   │   └── __init__.py
│   │   └── routes.py
│   │   └── schemas.py
│   ├── config/
│   │   └── __init__.py
│   │   └── logging.py
│   │   └── prompts.py
│   │   └── settings.py
│   ├── core/
│   │   └── __init__.py
│   │   └── agent.py
│   │   └── concepts.py
│   │   └── memory.py
│   │   └── reasoning.py
│   ├── rag/
│   │   └── __init__.py
│   │   └── chunking.py
│   │   └── embeddings.py
│   │   └── ingestion.py
│   │   └── retrieval.py
│   ├── storage/
│   │   ├── metadata/
│   │   ├── vectorstore/
│   │   └── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   │   └── test_ingestion.py
│   └── main.py
├── docs/
│   └── agent-status.md
│   └── architecture.md
│   └── roadmap.md
│   └── vision.md
├── experiments/
│   └── concept_mapping.ipynb
│   └── reasoning_playground.ipynb
├── frontend/
│   ├── box/
│   ├── website/
│   │   └── ask.html
│   │   └── index.html
│   │   └── status.html
├── integrations/
│   ├── boxsupe/
│   ├── papersupe/
│   │   └── README.md
└── .env.example
└── .gitignore
└── LICENSE
└── README.md
└── project_stx.txt
└── pyproject.toml
└── stx.py

```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/papersupe/agent-circle.git
cd agent-circle
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies:**

* `fastapi` – API framework
* `uvicorn` – ASGI server
* `pydantic` / `pydantic-settings` – Data validation and settings
* `pdfplumber` – PDF text extraction
* `loguru` – Structured logging

### 3. Add your PDFs

Place PDFs in:

```
backend/data/papers/
```

---

## Running the Backend

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

Endpoints:

| Endpoint         | Description                           |
| ---------------- | ------------------------------------- |
| `/`              | Root endpoint, returns service info   |
| `/api/v1/status` | Returns agent status and capabilities |
| `/docs`          | Swagger UI for API exploration        |

---

## Ingest Papers

Run the ingestion pipeline:

```bash
python backend/rag/ingestion.py
```

* Extracted text is stored in `backend/storage/processed/`
* Metadata JSON is stored in `backend/storage/metadata/`
* Logs are printed to stdout using `loguru`

Example metadata output (`.json`):

```json
{
  "title": "2512.24880v1",
  "authors": [],
  "year": "",
  "venue": "",
  "file_name": "backend/data/papers/2512.24880v1.pdf"
}
```

---

## Architecture Overview

* **Backend** – FastAPI app using Pydantic v2 and modular routers.
* **RAG Pipeline** – PDF ingestion, text processing, and metadata storage.
* **Logging** – Loguru provides INFO, SUCCESS, WARNING, and ERROR levels.
* **API Versioning** – Ready for `/api/v1` and future endpoints like `/agents`, `/concepts`, `/papers`.

---

## Roadmap

* [ ] Automatic extraction of authors, venue, and year from PDFs
* [ ] Concept linking & knowledge graph generation
* [ ] Embedding-based retrieval for reasoning (RAG)
* [ ] Interactive agent interface for querying papers
* [ ] Modular API expansion with `/agents`, `/concepts`, `/papers` endpoints

---

## References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic v2 Migration Guide](https://docs.pydantic.dev/2.12/migration/)
* [Loguru Logging](https://loguru.readthedocs.io/en/stable/)
* [pdfplumber PDF Extraction](https://github.com/jsvine/pdfplumber)

---

## License

MIT License – see `LICENSE` for details.

