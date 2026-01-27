def positive(lst):
    ans = []
    for i in lst:
        if i > -1:
            ans.append(i)

    return ans

print(positive([3, 5, 1, -6, -3, 0, -1, 5, 3]))