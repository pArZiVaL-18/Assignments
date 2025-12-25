def contains_sublist(main_list, sub_list):
    n = len(main_list)
    m = len(sub_list)

    if m == 0:
        return True

    for i in range(n - m + 1):
        if main_list[i:i + m] == sub_list:
            return True

    return False

print(contains_sublist([1, 2, 3, 4, 5], [3, 4]))
print(contains_sublist([1, 2, 3, 4, 5], [2, 4]))
print(contains_sublist([1, 2, 3], []))           
