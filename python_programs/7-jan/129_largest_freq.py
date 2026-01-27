# Write a function to find the item with maximum frequency in a given list.
from collections import Counter
def get_max_freq(lst):
    freq = Counter(lst)
    return max(freq, key=freq.get)

print(get_max_freq([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,4,4,4,3,3,2,2,1,11, 1, 1]))