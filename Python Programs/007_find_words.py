import re

def find_words(text):
    pattern = r'\b\w{4,}\b'
    return re.findall(pattern, text)

print(find_words("This is a test text with some four letter words like test, code, and more."))