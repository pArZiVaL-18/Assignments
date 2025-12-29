import re

def split_multiple_delimiters(s, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, s)

print(split_multiple_delimiters("roshan,pratik/rohit;kartik", [",", ";", "/"]))
