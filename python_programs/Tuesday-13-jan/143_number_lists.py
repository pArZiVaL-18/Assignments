def get_of_num_list(tup):
    count = 0
    for item in tup:
        if isinstance(item, list):
            count += 1
        
    return count

print(get_of_num_list(([1, 2, 3, 4, 2], 3, [4, 5], "roshan")))