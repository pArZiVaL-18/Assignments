def sum_of_negative(lst):
    negatives = list(filter(lambda item: item < 0, lst))

    return sum(negatives)

print(sum_of_negative([4, 6, 2, 9, 7, -3, -8, -5, -1]))