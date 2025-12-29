import re

def match_word(word, text):
    pattern = re.escape(word)
    return bool(re.match(word, text))


print(match_word("*Hello", "Hello world"))