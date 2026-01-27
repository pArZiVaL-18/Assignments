def next_power_of_2_bitwise(n):
    if n <= 1:
        return 1
    
    if (n & (n - 1)) == 0:
        return n
    
    power = 1
    while power < n:
        power <<= 1
    return power


def next_power_of_2_iterative(n):
    if n <= 1:
        return 1
    power = 1
    while power < n:
        power *= 2
    return power


nums = [0, 1, 5, 16, 17, 31, 64, 100]
print("Iterative :")
for n in nums:
    print(f"{n} -> {next_power_of_2_iterative(n)}")

print("Bit Manipulation :")
for n in nums:
    print(f"{n} -> {next_power_of_2_bitwise(n)}")
