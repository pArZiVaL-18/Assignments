def sum_positive_series(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total


print(sum_positive_series(7))  
print(sum_positive_series(8)) 
