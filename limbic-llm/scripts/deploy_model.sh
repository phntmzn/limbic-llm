

#!/bin/bash

echo "🚀 Deploying Limbic LLM API..."

# Set working directory to script location
cd "$(dirname "$0")"/..

# Optional: activate virtualenv
# source venv/bin/activate

# Run the FastAPI app with uvicorn
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload