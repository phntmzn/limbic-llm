

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(content={"status": "ok", "message": "Limbic LLM API is healthy."})