import json
from pathlib import Path

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def test_train_data_format():
    train_path = Path("data/processed/train.json")
    assert train_path.exists(), "Train file missing"
    train_data = load_jsonl(train_path)
    assert isinstance(train_data, list)
    assert "prompt" in train_data[0] and "response" in train_data[0]

def test_val_data_format():
    val_path = Path("data/processed/val.json")
    assert val_path.exists(), "Validation file missing"
    val_data = load_jsonl(val_path)
    assert isinstance(val_data, list)
    assert "prompt" in val_data[0] and "response" in val_data[0]