
def min_rotations(s):
    n = len(s)
    for i in range(1, n + 1):
        rotated = s[i:] + s[:i]
        if rotated == s:
            return i
        
    return n

print(min_rotations("bca"))  
print(min_rotations("abc"))  
print(min_rotations("abab"))  