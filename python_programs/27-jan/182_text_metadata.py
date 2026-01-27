import re

def analyze_string(text):
    """
    Find uppercase, lowercase, numeric, and special characters using regex.
    
    Returns:
        dict with counts of each category
    """
    result = {
        "uppercase": len(re.findall(r"[A-Z]", text)),
        "lowercase": len(re.findall(r"[a-z]", text)),
        "digits": len(re.findall(r"[0-9]", text)),
        "special_characters": len(re.findall(r"[^A-Za-z0-9]", text))
    }
    return result


s = "Hello@123 World!"

output = analyze_string(s)
print(output)
