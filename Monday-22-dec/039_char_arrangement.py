from collections import Counter

def char_arrangement(s):
    if len(s) == 0:
        return False
    
    freq = Counter(s)
    max_value = max(freq.values())

    if((len(s) + 1) // 2 >= max_value):
        return True
    
    return False

print(char_arrangement("aab"))    # True  -> "aba"
print(char_arrangement("aaab"))   # False
print(char_arrangement("abc"))    # True
print(char_arrangement("aaaa"))   # False
