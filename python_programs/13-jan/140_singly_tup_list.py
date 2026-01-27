from collections import Counter

def get_count_of_singly_tup_list(lst):
    singly_occurring = []
    counts = Counter(lst)
    print(counts)
    # singly_occurring = [item for item, count in counts.items() if count == 1]
    for item, count in counts.items():
        if count == 1:
            singly_occurring.append(item)
    
    return singly_occurring

print(get_count_of_singly_tup_list([(1, 2), (1, 2), (2, 3), (3, 2), (1, 5)]))