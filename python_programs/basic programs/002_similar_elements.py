def find_similar_elements(list1, list2):
    return list(set(list1) & set(list2))


list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [(3, 4), (7, 8), (1, 2), (3, 4)]
print(find_similar_elements(list1, list2))
