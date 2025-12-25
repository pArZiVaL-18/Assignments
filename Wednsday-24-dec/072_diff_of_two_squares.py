def is_difference_of_two_square(a, b):
    return a**2 - b**2 == (a - b)*(a + b)

print(is_difference_of_two_square(2, 3))
print(is_difference_of_two_square(5, 2))
print(is_difference_of_two_square(3, 4))