# Define different teaching styles and their attributes
teaching_styles = {
    "standard": {
        "name": "Standard",
        "description": "Clear and straightforward explanations with a balanced approach.",
        "prompt_prefix": "Provide a clear, step-by-step solution to this math problem using standard notation and explanations:",
        "detail_level": "medium",
        "tone": "neutral"
    },
    "detailed": {
        "name": "Detailed",
        "description": "Very thorough explanations with extensive breakdowns of each step.",
        "prompt_prefix": "Provide an extremely detailed solution to this math problem. Break down every step into smaller components and explain each concept thoroughly:",
        "detail_level": "high",
        "tone": "explanatory"
    },
    "simplified": {
        "name": "Simplified",
        "description": "Uses simpler language and basic explanations for beginners.",
        "prompt_prefix": "Solve this math problem using the simplest possible explanations and basic language. Avoid complex terminology and focus on fundamental concepts:",
        "detail_level": "low",
        "tone": "simple"
    },
    "visual": {
        "name": "Visual-oriented",
        "description": "Emphasizes visual representations and diagrams when applicable.",
        "prompt_prefix": "Solve this math problem with a focus on visual representations. Describe any diagrams, graphs, or visual aids that would help understand the solution. Use markdown formatting to create visual elements when possible:",
        "detail_level": "medium",
        "tone": "descriptive"
    },
    "socratic": {
        "name": "Socratic",
        "description": "Guides through the solution by asking leading questions.",
        "prompt_prefix": "Solve this math problem using the Socratic method. Guide the student with thoughtful questions at each step, then provide the answers to those questions:",
        "detail_level": "medium",
        "tone": "inquisitive"
    }
}

def apply_style(problem, style_attributes):
    """
    Apply a teaching style to the math problem prompt.
    
    Args:
        problem (str): The original math problem
        style_attributes (dict): The attributes of the selected teaching style
        
    Returns:
        str: The styled prompt to send to the API
    """
    styled_prompt = f"{style_attributes['prompt_prefix']}\n\nProblem: {problem}\n\n"
    
    # Add more specific instructions based on the style
    if style_attributes["detail_level"] == "high":
        styled_prompt += "Provide extensive explanations for each step. Don't skip any details.\n"
    elif style_attributes["detail_level"] == "low":
        styled_prompt += "Focus on the core concepts and keep explanations brief but clear.\n"
    
    if style_attributes["tone"] == "inquisitive":
        styled_prompt += "Format your response as a series of guiding questions followed by answers.\n"
    elif style_attributes["tone"] == "simple":
        styled_prompt += "Use everyday language and avoid complex mathematical terminology when possible.\n"
    elif style_attributes["tone"] == "descriptive":
        styled_prompt += "Describe visual representations that would aid understanding, using markdown to create diagrams where applicable.\n"
    
    return styled_prompt
