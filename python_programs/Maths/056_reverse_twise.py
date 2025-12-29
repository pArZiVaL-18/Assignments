def is_one_less_than_twice_reverse(n):
    reverse_n = int(str(n)[::-1])
    
    return n == 2 * reverse_n - 1


print(is_one_less_than_twice_reverse(12))  
print(is_one_less_than_twice_reverse(23))  