

import pytest

def mock_model_inference(prompt: str, max_tokens: int = 50):
    # Simulated inference response
    return f"Generated response for: {prompt[:max_tokens]}"

def test_model_inference_output():
    prompt = "What is the capital of France?"
    result = mock_model_inference(prompt, max_tokens=30)
    assert isinstance(result, str)
    assert result.startswith("Generated response for:")
    assert "France" in result