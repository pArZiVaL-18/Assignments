def max_diff(lst):
    ans = [abs(a-b) for a, b in lst]
    return max(ans)

print(max_diff([(1, 2), (4, 7), (2, 9)]))