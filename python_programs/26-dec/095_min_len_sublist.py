def min_length_sublist(lst):
    min_len = len(lst[0])
    for item in lst:
        if len(item) < min_len:
            min_len = len(item)
    
    return min_len


print(min_length_sublist([[1, 2, 3, 5], [6, 5, 4], [4, 3], [3]]))
print(min_length_sublist([[1, 2, 3, 5], [6, 5, 4], [4, 3], [3, 3, 3, 3, 3]]))
print(min_length_sublist([[]]))