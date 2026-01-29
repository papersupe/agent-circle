# backend/api/routes.py

from fastapi import APIRouter
from backend.api.search import router as search_router

router = APIRouter()

@router.get("/status")
def agent_status():
    return {
        "name": "Agent Circle",
        "status": "Experimental",
        "mode": "Reading-Only",
        "capabilities": [
            "semantic_search",
            "paper_ingestion",
            "evidence_lookup"
        ],
        "interaction": "enabled"
    }

router.include_router(search_router)

