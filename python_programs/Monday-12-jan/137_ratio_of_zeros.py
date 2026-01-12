def get_ratio_of_zeros(lst):
    zeros = 0
    for num in lst:
        if num == 0:
            zeros += 1

    return zeros / len(lst)


print(get_ratio_of_zeros([3, 2, 4, 1, 0, 7, 0, 0, 0, 5]))