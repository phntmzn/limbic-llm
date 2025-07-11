

import argparse
import json
from pathlib import Path
from src.config import load_config

def train_model(config):
    print("Training model with config:")
    print(json.dumps(config, indent=2))

    # Simulated training loop
    steps_per_epoch = 5
    training_log = []
    for epoch in range(config["training"]["epochs"]):
        for step in range(steps_per_epoch):
            step_count = epoch * steps_per_epoch + step + 1
            train_loss = 2.5 - 0.1 * step_count
            val_loss = 2.4 - 0.08 * step_count
            log_entry = {
                "step": step_count,
                "train_loss": round(train_loss, 4),
                "val_loss": round(val_loss, 4),
                "accuracy": round(0.6 + 0.01 * step_count, 4)
            }
            print(f"Epoch {epoch+1}, Step {step+1}: {log_entry}")
            training_log.append(log_entry)

    # Save log
    log_dir = Path(config["output"]["log_dir"])
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_dir / "train_log.json", "w") as f:
        json.dump(training_log, f, indent=2)

    print(f"Saved training log to {log_dir / 'train_log.json'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
    args = parser.parse_args()

    config = load_config(args.config)
    train_model(config)