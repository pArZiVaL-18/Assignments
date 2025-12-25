def sum(lst):
    if not lst:
        return 0
    
    return lst[0] + sum(lst[1:])

print(sum([1, 2, 3, 4, 5, 6]))