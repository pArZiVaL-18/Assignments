def largest_prime_factor(n):
    largest = -1

    while n % 2 == 0:
        largest = 2
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2

    if n > 1:
        largest = n

    return largest

print(largest_prime_factor(68))