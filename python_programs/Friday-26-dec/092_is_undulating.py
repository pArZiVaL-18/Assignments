def is_undulating(n):
    n = str(n)
    if len(n) <= 2:
        return False
    
    for i in range(2, len(n)):
        if n[i-2] != n[i]:
            return False
        
    return True

print(is_undulating(1212121))
print(is_undulating(12321))