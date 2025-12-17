def binomial_coefficient(n, k):
    if k > n:
        return 0
    
    k = min(k, n - k)
    
    numerator = 1
    denominator = 1

    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    
    return numerator // denominator


print(binomial_coefficient(5, 2))  # Output: 10
print(binomial_coefficient(10, 3))  # Output: 120