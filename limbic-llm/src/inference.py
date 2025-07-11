

import argparse
from src.config import load_config

def run_inference(prompt, config):
    # Placeholder inference logic
    return f"[Generated text for prompt: '{prompt[:50]}']"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt for inference")
    args = parser.parse_args()

    config = load_config(args.config)
    result = run_inference(args.prompt, config)
    print(result)