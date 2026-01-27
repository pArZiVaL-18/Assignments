from collections import Counter

def sum_of_repeated_numbers(lst):
    freq = Counter(lst)

    return sum([num for num, count in freq.items() if count > 1])


print(sum_of_repeated_numbers([1, 2, 2, 3, 3, 4, 4, 5, 5, 1, ]))