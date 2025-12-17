import re

def split_at_lowercase(s):
    parts = re.split(r'[a-z]', s)
    print(parts)  # Debugging statement to show intermediate result
    result = [part for part in parts if part]
    return result


# Example usage:
print(split_at_lowercase("HeLLoRoWorld"))  # Output: ['H', 'LL', 'W']
print(split_at_lowercase("PYTHON"))      # Output: ['PYTHON']
print(split_at_lowercase("abc"))         # Output: []
