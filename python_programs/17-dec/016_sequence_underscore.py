import re

def find_lowercase_underscore_sequences(s):
    pattern = r'\b[a-z]+[_]+[a-z]+\b'
    return re.findall(pattern, s)


text = "valid: abc_def, x_y; invalid: Abc_def, abc__def, hello-World"
print(find_lowercase_underscore_sequences(text))
