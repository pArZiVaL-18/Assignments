def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


print(is_coprime(14, 15))  
print(is_coprime(12, 18)) 
