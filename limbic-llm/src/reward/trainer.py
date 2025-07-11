import random
from src.reward.reward_model import score_response
from src.inference import run_inference

def reward_guided_training(prompts, config):
    log = []
    for i, prompt in enumerate(prompts):
        # Get model output
        response = run_inference(prompt, config)

        # Compute reward score
        reward = score_response(prompt, response)

        # Log result
        print(f"[{i+1}] Prompt: {prompt}")
        print(f"Response: {response}")
        print(f"Reward: {reward:.3f}\n")

        log.append({
            "prompt": prompt,
            "response": response,
            "reward": reward
        })

    return log

if __name__ == "__main__":
    # Example config and prompt list
    example_config = {
        "reward_model": {
            "target_emotion": "joy"
        }
    }
    example_prompts = [
        "Tell me something inspiring.",
        "What should I do when I feel anxious?",
        "How do you define success?"
    ]
    reward_guided_training(example_prompts, example_config)
