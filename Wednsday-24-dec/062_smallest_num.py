def smallest_num(lst):
    minval = lst[0]
    for i in range(1, len(lst)):
        if minval > lst[i]:
            minval = lst[i]
    
    return minval

print(smallest_num([5, 4, 3, 6, 7, 2, 8, 1, 9]))