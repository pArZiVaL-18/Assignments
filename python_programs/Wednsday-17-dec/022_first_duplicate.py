def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num  # first duplicate found
        seen.add(num)
    return -1  

print(first_duplicate([2, 1, 3, 5, 3, 2]))  # Output: 3
print(first_duplicate([1, 2, 3, 4, 5]))     # Output: -1
