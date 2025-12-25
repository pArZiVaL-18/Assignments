def set_all_odd_bits_loop(n):
    bit_pos = 1  # start from first odd bit

    while bit_pos < n.bit_length()+1:
        n = n | (1 << bit_pos)
        bit_pos += 2
        
    print(n)
    return bin(n)

def set_all_odd_bits(n):
    mask = 0xAAAAAAAA
    print(n | mask)
    return bin(n | mask)


print(set_all_odd_bits_loop(13))
print(set_all_odd_bits(13))
