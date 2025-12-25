from collections import Counter

def freq(main_list):
    flatten = []

    for i in range(len(main_list)):
        for j in range(len(main_list[i])):
            flatten.append(main_list[i][j])

    
    freq = Counter(flatten)

    return freq

print(freq([[2, 3, 4, 6], [1, 2, 3, 5], [7, 6, 8, 2]]))