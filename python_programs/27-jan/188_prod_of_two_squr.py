import math

def is_product_of_two_squares(n):
    if n < 0:
        return False

    root = int(math.isqrt(n))
    return root * root == n


print(is_product_of_two_squares(36))   
print(is_product_of_two_squares(18))   
print(is_product_of_two_squares(49))   
print(is_product_of_two_squares(50))   