def is_equal(lst):
    n = len(lst[0])

    for element in lst:
        if len(element) != n:
            return False
        
    return True


print(is_equal([(1, 2, 3), (3, 4, 2)]))
print(is_equal([(1, 2, 3), (3, 4, 2), (4, 7)]))