

#!/bin/bash

echo "🧠 Starting training for Limbic LLM..."

# Set working directory to script location
cd "$(dirname "$0")"/..

# Optional: activate virtualenv
# source venv/bin/activate

# Run the training script
python src/train.py --config experiments/config_1.yaml