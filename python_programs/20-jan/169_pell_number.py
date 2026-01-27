def pell_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * pell_recursive(n-1) + pell_recursive(n-2)

def pell_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    n_minus_one, n_minus_two = 0, 1
    for _ in range(2, n + 1):
        curr = 2 * n_minus_two + n_minus_one
        n_minus_one, n_minus_two = n_minus_two, curr
    return n_minus_two


print(pell_recursive(5))
print(pell_recursive(7))
print(pell_iterative(5))
print(pell_iterative(7))