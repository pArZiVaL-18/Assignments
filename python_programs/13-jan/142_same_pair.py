def count_same_pairs(list1, list2, list3):
    count = 0
    for a, b, c in zip(list1, list2, list3):
        if a == b == c:
            count += 1
    return count


print(count_same_pairs([1, 2, 3, 4], [1, 4, 3, 2], [1, 2, 3, 5]))