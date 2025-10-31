from fastapi import Header, HTTPException, status
from app.config import settings

def verify_api_key(x_api_key: str = Header(None)):
    """
    Verifies that x-api-key header matches configured API_KEY.
    If no API key is configured in .env, return 401 to encourage secure setup.
    """
    if not settings.api_key:
        # No API key configured at runtime — treat as not authorized to protect endpoints
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key not configured on server")

    if x_api_key is None or x_api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid x-api-key")
