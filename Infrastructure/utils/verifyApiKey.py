from fastapi import Header, HTTPException, status
from Infrastructure.utils.configuration import *


async def verify_api_key(api_key: str = Header(..., alias="X-API-Key")):
    if not api_key or api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Proporcione una API Key válida",
            headers={"WWW-Authenticate": "API-Key"},
        )
