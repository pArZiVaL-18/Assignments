def my_largest_prime_factor(n):
    ans = -1

    while n % 2 == 0:
        ans = 2
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            ans = factor
            n //= factor

        factor += 2

    if n > 1:
        ans = n

    return ans

print(my_largest_prime_factor(48))