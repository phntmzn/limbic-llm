

from fastapi import FastAPI
from api.routes import health, inference

app = FastAPI(
    title="Limbic LLM API",
    description="API for interacting with the Limbic Language Model",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(inference.router)