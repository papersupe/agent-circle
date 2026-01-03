# backend/api.routes.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def agent_status():
    return {
        "name": "Agent Circle",
        "status": "Experimental",
        "mode": "Reading-Only",
        "capabilities": [
            "paper_ingestion",
            "concept_extraction",
            "concept_linking"
        ],
        "interaction": "disabled"
    }
