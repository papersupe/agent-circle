from fastapi import FastAPI
from backend.api.routes import router
from backend.config.logging import setup_logging
from backend.config.settings import settings

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title="Agent Circle",
        description="Experimental research intelligence system (Reading-Only)",
        version="0.1.0"
    )

    app.include_router(router)

    return app

app = create_app()
