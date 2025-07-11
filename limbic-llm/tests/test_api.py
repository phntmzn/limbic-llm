

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Limbic LLM API is healthy."}

def test_inference_endpoint():
    payload = {"prompt": "Once upon a time", "max_tokens": 50}
    response = client.post("/inference", json=payload)
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"].startswith("Generated response for")