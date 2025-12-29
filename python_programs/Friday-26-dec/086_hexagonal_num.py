def nth_hexagonal(n):
    return n*(2 * n - 1)

def centered_hexagonal_num(n):
    return 3 * n * (n + 1) + 1

ans = []
ans2 = []
for i in range(1, 10):
    ans.append(nth_hexagonal(i))
    ans2.append(centered_hexagonal_num(i))


print(ans)
print(ans2)