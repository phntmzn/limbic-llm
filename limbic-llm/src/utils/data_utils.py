

import json
from pathlib import Path

def load_jsonl(path):
    """
    Load a JSONL (JSON Lines) file and return a list of dictionaries.
    """
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def save_jsonl(data, path):
    """
    Save a list of dictionaries to a JSONL file.
    """
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")