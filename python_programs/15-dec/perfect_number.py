def is_perfect(n):
    """
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors,
    excluding itself. For example, 6 is a perfect number because its divisors are 1, 2, and 3,
    and 1 + 2 + 3 = 6.
    """
    
    if n <= 1:
        return False

    sum = 0
    num = n

    while num > 1:
        num -= 1
        if n % num == 0:
            sum += num

    return sum == n 


def find_perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

print(find_perfect_numbers_in_range(1, 100))