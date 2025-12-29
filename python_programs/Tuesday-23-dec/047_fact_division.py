def factorial(n):
    if n < 0:
        return -1
    ans = 1
    while n > 0:
        ans *= n
        n -= 1
    return ans

def factorial_division(a, b):
    if a > b:
        return -1
    
    ans = 1
    # ans = factorial(b)//factorial(a)
    for i in range(a+1, b+1):
        ans = ans * i

    print(ans)
    return ans%10

print(factorial_division(3, 5))