from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/health", tags=["Health"])

@router.get("/")
def health_check():
    """
    Simple public health check used by the client:
    GET /api/v1/health -> { "status": "ok" }
    """
    return {"status": "ok"}
