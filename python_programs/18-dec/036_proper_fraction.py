def proper_fraction(a, b, n):
    if a > b: 
        print("The fraction must be proper (a < b)")
    
    if n < 0:
        print("n must be positive")
        
    while n > 0:
        rem = a % b
        a = rem * 10
        digit = a // b
        n -= 1

    return digit

print(proper_fraction(-13, 7, 1))
