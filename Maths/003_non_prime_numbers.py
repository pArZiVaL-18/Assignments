# It returns if a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# function to traverse a list and fetch non-prime numbers
def identify_non_primes(numbers):
    non_primes = [n for n in numbers if not is_prime(n)]
    return non_primes


# sample execution
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(identify_non_primes(nums))
