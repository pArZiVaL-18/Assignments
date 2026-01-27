def max_product(lst):
    ans = 0
    for num1, num2 in lst:
        ans = max(ans, num1 * num2)

    return ans

print(max_product([(2, 3), (2, 1), (5, 5), (10, 2)]))