def is_equilateral(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return a == b == c
    return False

print(is_equilateral(2, 4, 3))
print(is_equilateral(2, 2, 4))
print(is_equilateral(4, 4, 4))