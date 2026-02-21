from prompts.system_prompt import SYSTEM_PROMPT

def build_prompt(user_input):
    """
    Build clean prompt without re-injecting full history.
    Gemini chat session already maintains memory.
    """
    final_prompt = f"""
User Question:
{user_input}

Provide structured career guidance.
"""
    return final_prompt