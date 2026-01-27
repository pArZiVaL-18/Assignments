def max_sum_in_list_of_lists(lst):
    return max(sum(sublist) for sublist in lst)

lists = [[1, 2, 3], [4, 5], [10, -2], [0, 0, 1]]
print(max_sum_in_list_of_lists(lists))
