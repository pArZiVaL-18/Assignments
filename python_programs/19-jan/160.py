def find_xy(a, b, n):
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if a * x + b * y == n:
                return x, y
    return None


a = 4
b = 6
n = 14

print(find_xy(a, b, n)) 
