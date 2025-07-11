# 🧠 Limbic LLM

Limbic LLM is a modular framework for fine-tuning, evaluating, and serving large language models. It is designed for fast experimentation, clear separation of concerns, and production-ready deployment.

## 📦 Features

- Fine-tuning with YAML-configurable hyperparameters
- Evaluation logging and metrics visualization
- FastAPI-based API for inference
- Config-driven training pipeline
- Scripted deployment and testing

## 🧠 Limbic-Inspired Flow

```
[Input Prompt]
   ↓
[Emotion Detector] → [Emotion Embedding]
   ↓
[Motivation Manager] → [Policy Router]
   ↓
[Salient Memory Retrieval (VectorStore)]
   ↓
[LLM Generation]
   ↓
[Reward Model Feedback (if training)]
```

## 📁 Project Structure

```
limbic-llm/
├── src/              # Core training, evaluation, inference logic
├── api/              # FastAPI app and routes
├── data/             # Raw and processed datasets
├── models/           # Base models, checkpoints, adapters
├── notebooks/        # EDA, visualization, experiments
├── scripts/          # Shell scripts to run/train/evaluate/deploy
├── experiments/      # Logs and YAML configs
└── tests/            # Pytest unit tests
```

## 🚀 Quickstart

**1. Install dependencies (with Poetry):**
```bash
poetry install
```

**2. Run training:**
```bash
bash scripts/run_train.sh
```

**3. Run evaluation:**
```bash
bash scripts/run_eval.sh
```

**4. Serve the model:**
```bash
bash scripts/deploy_model.sh
```

**5. Test the API:**
```bash
pytest tests/
```

## 📜 License

MIT License