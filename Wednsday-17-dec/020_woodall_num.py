def is_woodall(n):
    k = 1
    while True:
        value = k * (2 ** k) - 1
        if value == n:
            return True
        if value > n:
            return False
        k += 1


print(is_woodall(7))    # True → 2·2² − 1 = 7
print(is_woodall(23))   # True → 3·2³ − 1 = 23
print(is_woodall(15))   # False
