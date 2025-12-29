def divisible(lst, k):
    ans = []
    for tup in lst:
        is_divisible = True
        for i in tup:
            if i % k != 0:
                is_divisible = False
        if is_divisible:
            ans.append(tup)
        
    return ans

print(divisible([(3, 6, 9), (2, 5, 8, 4), (8, 5, 3)], 3))
print(divisible([(3, 6, 9), (2, 10, 8, 4), (8, 5, 3)], 2))
print(divisible([(3, 6, 9), (2, 5, 8, 4), (8, 5, 3), (3, 18)], 3))