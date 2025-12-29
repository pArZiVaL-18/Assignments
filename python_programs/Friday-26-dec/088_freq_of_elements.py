def freq(lst):
    d = dict()
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

print(freq([1, 3, 2, 4, 3, 2, 4, 1, 2, 3]))

