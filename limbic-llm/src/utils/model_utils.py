

from transformers import AutoTokenizer, AutoModelForCausalLM

def load_tokenizer(model_name):
    """
    Load a tokenizer from Hugging Face by model name or path.
    """
    return AutoTokenizer.from_pretrained(model_name)

def load_model(model_name):
    """
    Load a causal language model from Hugging Face by model name or path.
    """
    return AutoModelForCausalLM.from_pretrained(model_name)