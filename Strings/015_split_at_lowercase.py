import re

def split_at_lowercase(s):
    parts = re.split(r'[a-z]', s)
    result = [part for part in parts if part]
    return result


# Example usage:
print(split_at_lowercase("HeLLoWorld"))  # Output: ['H', 'L', 'L', 'W']
print(split_at_lowercase("PYTHON"))      # Output: ['PYTHON']
print(split_at_lowercase("abc"))         # Output: []
