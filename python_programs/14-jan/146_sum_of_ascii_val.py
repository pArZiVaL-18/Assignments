def ascii_total(s):
    total = 0
    for ch in s:
        total += ord(ch)
    return total


print(ascii_total("ABC")) 
