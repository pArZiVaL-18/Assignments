from collections import Counter

def find_odd_occurring_elements(arr):
    freq = Counter(arr)
    return [x for x, count in freq.items() if count % 2 != 0]



arr = [1, 2, 3, 2, 3, 1, 3, 4, 4, 5, 5, 5, 10, 5]
odd_elements = find_odd_occurring_elements(arr)
print(odd_elements)
