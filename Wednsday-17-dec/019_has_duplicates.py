def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


def has_duplicates_using_built_in(arr):
    return len(arr) != len(set(arr))



print(has_duplicates([1, 2, 3, 4, 5]))     # False
print(has_duplicates([1, 3, 2, 4, 2, 5]))  # True
print(has_duplicates_using_built_in([1, 2, 3, 4, 5]))     # False
print(has_duplicates_using_built_in([1, 3, 2, 4, 2, 5]))  # True
