from fastapi import FastAPI
from app.api.routes import health, status
from app.core.logger import logger

app = FastAPI(title="Headless AI RAG Agent", version="1.0.0")

# Register routers
app.include_router(health.router)
app.include_router(status.router)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Headless AI RAG Agent is running"}
