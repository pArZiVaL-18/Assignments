def multiples_of_n(n, m):
    return [n * i for i in range(1, m + 1)]


print(multiples_of_n(3, 5))  # [3, 6, 9, 12, 15]
print(multiples_of_n(7, 4))  # [7, 14