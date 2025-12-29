def get_min_len(lst):
    return min(lst, key=lambda x: len(x))


print(get_min_len([[1,2,4],[6,5,7,4],[8,9,0,2, 2]]))
print(get_min_len([[1,2,4],[7,4],[8,9,0,2, 2]]))