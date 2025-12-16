def differ_by_one_bit(a, b):
    xor_value = a ^ b
    return xor_value != 0 and (xor_value & (xor_value - 1)) == 0

# Example usage
print(differ_by_one_bit(10, 8))   
print(differ_by_one_bit(10, 15))  
