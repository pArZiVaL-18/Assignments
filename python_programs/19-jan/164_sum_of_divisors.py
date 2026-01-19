def same_sum_of_divisors(a, b):
    def sum_of_divisors(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i
        return total

    return sum_of_divisors(a) == sum_of_divisors(b)

print(same_sum_of_divisors(6, 8))
print(same_sum_of_divisors(6, 6))
