def largest_number_from_digits(digits):
    digits_sorted = sorted(digits, reverse=True)
    
    number_str = ''.join(str(d) for d in digits_sorted)
    
    return int(number_str)

print(largest_number_from_digits([3, 1, 4, 1, 5, 9]))  
print(largest_number_from_digits([0, 2, 5, 7]))