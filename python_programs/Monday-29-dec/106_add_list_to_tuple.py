def add_list_to_tuple(lst, tup):
    tup = list(tup)
    tup.append(lst)
    tup = tuple(tup)
    return tup
    # return tuple(list(tup).append(lst))


print(add_list_to_tuple([1, 2, 3, 4], ([1, 2], [6, 5])))