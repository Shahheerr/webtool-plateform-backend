"""
Deterministic Tools Module
Non-AI tools that perform specific operations without LLM calls.
"""


def hex_to_rgb_logic(input_data: str) -> str:
    """Convert hex color to RGB format.
    
    Args:
        input_data: Hex color code (with or without #)
        
    Returns:
        RGB string or error message
    """
    hex_val = input_data.lstrip('#').strip()
    try:
        if not hex_val:
            return "Error: Please provide a hex color code"
        
        # Handle shorthand (e.g., #FFF -> #FFFFFF)
        if len(hex_val) == 3:
            hex_val = ''.join([c*2 for c in hex_val])
        
        if len(hex_val) != 6:
            return f"Error: Invalid hex code length. Expected 6 characters, got {len(hex_val)}"
        
        r = int(hex_val[0:2], 16)
        g = int(hex_val[2:4], 16)
        b = int(hex_val[4:6], 16)
        return f"rgb({r}, {g}, {b})"
    except ValueError:
        return "Error: Invalid hex characters. Use 0-9 and A-F only"


def code_beautifier_logic(input_data: str) -> str:
    """Beautify code with proper formatting.
    
    Args:
        input_data: Code string to beautify
        
    Returns:
        Beautified code string
    """
    if not input_data or not input_data.strip():
        return "Error: Please provide code to beautify"
    
    lines = input_data.strip().split('\n')
    beautified = '\n'.join(line.rstrip() for line in lines)
    return beautified


def domain_checker_logic(input_data: str) -> str:
    """Check domain availability (mock implementation).
    
    Args:
        input_data: Domain name to check
        
    Returns:
        Availability status (mock)
    """
    domain = input_data.strip().lower().replace(' ', '').replace('http://', '').replace('https://', '')
    
    if not domain:
        return "Error: Please provide a domain name"
    
    # Remove existing TLD if present
    if '.' in domain:
        domain = domain.split('.')[0]
    
    # Mock response - in production, this would check actual availability
    return f"Domain '{domain}.com' appears to be available! (Mock Check)"


def plagiarism_checker_logic(input_data: str) -> str:
    """Check for plagiarism (mock implementation).
    
    Args:
        input_data: Text to check
        
    Returns:
        Plagiarism check result (mock)
    """
    text = input_data.strip()
    
    if not text:
        return "Error: Please provide text to check for plagiarism"
    
    word_count = len(text.split())
    char_count = len(text)
    
    # Mock response
    return f"Plagiarism Check Complete.\n- Originality Score: 95%\n- Words Analyzed: {word_count}\n- Characters: {char_count}"
