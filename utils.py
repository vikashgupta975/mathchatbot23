import os
import requests
import json

def get_mistral_response(prompt):
    """
    Get a response from Mistral AI API for the given math problem prompt.
    
    Args:
        prompt (str): The math problem prompt with style instructions
        
    Returns:
        str: The formatted response from Mistral AI
    """
    # Get API key from environment variable
    api_key = os.getenv("MISTRAL_API_KEY")
    
    if not api_key:
        return "Error: Mistral AI API key not found. Please set the MISTRAL_API_KEY environment variable."
    
    # Mistral AI API endpoint
    url = "https://api.mistral.ai/v1/chat/completions"
    
    # Prepare the full prompt with instructions
    full_prompt = f"""
    You are a specialized math tutor. Your task is to solve the following math problem step-by-step:
    
    {prompt}
    
    Provide a clear, detailed, and accurate solution. Break down complex steps into simpler ones.
    Use proper mathematical notation and explain your reasoning at each step.
    """
    
    # Prepare the payload
    payload = {
        "model": "mistral-medium",  # You can change this to other available models
        "messages": [
            {"role": "system", "content": "You are a helpful math tutor assistant."},
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.2,  # Lower temperature for more deterministic responses
        "max_tokens": 1000
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response
        result = response.json()
        
        # Extract the assistant's message
        if "choices" in result and len(result["choices"]) > 0:
            assistant_message = result["choices"][0]["message"]["content"]
            return assistant_message
        else:
            return "Error: Unexpected response format from Mistral AI API."
    
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Mistral AI API: {str(e)}"
    except json.JSONDecodeError:
        return "Error: Invalid response from Mistral AI API."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
