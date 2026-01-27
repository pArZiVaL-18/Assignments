from collections import Counter

def get_tuple_freq(tuple_list):
    return Counter(tuple_list)

def get_tuple_frequency(tuple_list):
    freq = {}
    for tup in tuple_list:
        freq[tup] = freq.get(tup, 0) + 1
    return freq




tup = [(2, 3, 1), (1, 2, 3), (2, 3, 1), (1, 2), (1, 2), (1, 2)]
print(get_tuple_frequency(tup))
print(get_tuple_freq(tup))