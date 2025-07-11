

#!/bin/bash

echo "📊 Running evaluation for Limbic LLM..."

# Set working directory to script location
cd "$(dirname "$0")"/..

# Optional: activate virtualenv
# source venv/bin/activate

# Run the evaluation script
python src/evaluate.py --config experiments/config_1.yaml