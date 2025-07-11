


def route_generation_strategy(motivation):
    """
    Return generation strategy settings based on motivational state.
    """
    strategies = {
        "empathy": {
            "temperature": 0.7,
            "top_p": 0.9,
            "prefix": "With compassion,"
        },
        "curiosity": {
            "temperature": 1.0,
            "top_p": 0.95,
            "prefix": "Here's something intriguing:"
        },
        "safety": {
            "temperature": 0.5,
            "top_p": 0.85,
            "prefix": "Please stay calm and consider this:"
        },
        "assertiveness": {
            "temperature": 0.8,
            "top_p": 0.9,
            "prefix": "Let me be clear:"
        }
    }

    return strategies.get(motivation, {
        "temperature": 0.7,
        "top_p": 0.9,
        "prefix": ""
    })