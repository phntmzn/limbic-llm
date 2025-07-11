

import random

def select_motivation(context=None):
    """
    Select a motivational state based on input context or randomly.
    """
    motivations = ["empathy", "curiosity", "safety", "assertiveness"]

    if context:
        lowered = context.lower()
        if "help" in lowered or "sad" in lowered or "sorry" in lowered:
            return "empathy"
        if "learn" in lowered or "discover" in lowered or "why" in lowered:
            return "curiosity"
        if "danger" in lowered or "panic" in lowered or "emergency" in lowered:
            return "safety"
        if "decide" in lowered or "must" in lowered or "now" in lowered:
            return "assertiveness"

    return random.choice(motivations)