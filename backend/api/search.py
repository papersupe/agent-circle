from fastapi import APIRouter, Query, HTTPException
from typing import List

from backend.rag.chunk_lookup import lookup_chunks
from backend.rag.retrieval import retrieve

router = APIRouter()

@router.get("/search")
def search(
    q: str = Query(..., min_length=3),
    k: int = Query(5, ge=1, le=20)
):
    """
    Semantic search over ingested papers.
    Read-only, evidence-based.
    """

    try:
        hits = retrieve(q, top_k=k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    results = []
    for hit in hits:
        chunk_text = lookup_chunk(
            paper_id=hit["paper_id"],
            chunk_id=hit["chunk_id"]
        )

        results.append({
            "paper_id": hit["paper_id"],
            "chunk_id": hit["chunk_id"],
            "score": hit["score"],
            "text": chunk_text
        })

    return {
        "query": q,
        "results": results
    }
