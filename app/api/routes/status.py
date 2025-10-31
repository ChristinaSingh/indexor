from fastapi import APIRouter, Depends
from app.core.auth import verify_api_key
from app.config import settings
from app.core.logger import logger

router = APIRouter(prefix="/api/v1/status", tags=["Status"])

@router.get("/", dependencies=[Depends(verify_api_key)])
def get_status():
    """
    Returns configuration readiness and placeholder indexing info.
    - If required variables for later phases are missing, return {"status": "not_configured"}
    - Otherwise return a 'connecting' stub (real indexing will be added in Phase 2)
    """
    logger.info("Status endpoint called")

    # Define which env keys we consider "required" for proper configuration beyond phase 1.
    # For Phase 1 we only require API_KEY to authenticate; the client expects missing SOURCE_SYSTEM to be reported as not_configured.
    required_for_operation = [settings.source_system, settings.openrouter_key]

    # If any of the required future keys are missing/empty, report not_configured.
    if any(v is None or str(v).strip() == "" for v in required_for_operation):
        return {"status": "not_configured"}

    # Otherwise return the initial connecting state (placeholders)
    return {
        "status": "connecting",
        "indexed_docs": 0,
        "total_docs": 0,
        "failed_docs": 0,
        "progress_percentage": 0
    }
