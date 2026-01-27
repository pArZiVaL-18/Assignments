def has_all_k_elements(tuple_list, k):
    return all(len(t) == k for t in tuple_list)

data1 = [(1, 2), (3, 4), (5, 6)]
print(has_all_k_elements(data1, 2))   # True

data2 = [(1, 2), (3, 4, 5), (6, 7)]
print(has_all_k_elements(data2, 2))   # False

