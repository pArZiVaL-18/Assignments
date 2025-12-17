def remove_chars(s1, s2):
    remove_set = set(s2)
    return ''.join(ch for ch in s1 if ch not in remove_set)

s1 = "abcdefg"
s2 = "bd"
print(remove_chars(s1, s2))  # Output: "acefg"