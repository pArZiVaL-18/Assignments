from collections import Counter

# need to convert list of list to list of tuple so that they can be keys to dictionary
# lists are mutable so they cannot be keys

def get_freq(lst):
    temp = []
    for sub_list in lst:
        temp.append(tuple(sub_list))
    
    freq = Counter(temp)
    return freq



lst = [[1, 2], [3, 4], [1, 2], [5], [3, 4], [1, 2]]
print(get_freq(lst))