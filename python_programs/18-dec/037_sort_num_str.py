def sort_num_str_list(lst):
    numbers = sorted([n for n in lst if isinstance(n, int)])
    strings = sorted([n for n in lst if isinstance(n, str)])
    return numbers + strings


print(sort_num_str_list([1, 8, "abbb", 4, "bbdd", 2, "ffff", "cccc"]))