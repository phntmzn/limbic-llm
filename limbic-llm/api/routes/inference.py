

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class InferenceRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

class InferenceResponse(BaseModel):
    result: str

@router.post("/inference", response_model=InferenceResponse, tags=["Inference"])
async def generate_text(request: InferenceRequest):
    # Placeholder for actual model call
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    # Mocked response
    generated = f"Generated response for: {request.prompt[:50]}"
    return InferenceResponse(result=generated)