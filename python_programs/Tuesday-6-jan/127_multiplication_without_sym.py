def multiply(a, b):
    ans = 0
    for _ in range(b):
        ans += a
    return ans

print(multiply(5, 10))
print(multiply(2, 4))