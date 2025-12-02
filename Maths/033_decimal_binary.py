def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    bits = []
    
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    
    bits.reverse()
    
    return "".join(bits)


print(decimal_to_binary(10))  
print(decimal_to_binary(0))   
print(decimal_to_binary(255)) 
print(decimal_to_binary(4))   