def binary_to_decimal(binary_str):
    decimal = 0
    for i, bit in enumerate(reversed(binary_str)):
        if bit == '1':
            decimal += 2 ** i
    return decimal

# Example usage
binary_number = "1111"
print(f"Decimal of {binary_number} is {binary_to_decimal(binary_number)}")
