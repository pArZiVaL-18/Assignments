def toggle_bits(n):
    temp = n
    mask = 0
    count = 0
    while temp > 0 :
        if (count % 2 == 1):
            mask |= (1 << count)

        count+=1
        temp >>= 1
    
    return mask | n




print(toggle_bits(12))
print(toggle_bits(21))