def distinct(lst):
    return len(lst) == len(set(lst))

print(distinct([1,2,3,4, 5, 6,2,  7]))