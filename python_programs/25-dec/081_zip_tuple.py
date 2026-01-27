def zip_tuple(l1, l2):
    return tuple(zip(l1, l2))

def manual_zip(l1, l2):
    ans = []
    for i in range(min(len(l1), len(l2))):
        ans.append((l1[i], l2[i]))
    
    return tuple(ans)

print(zip_tuple([1, 2, 3], ["a", "b", "c"]))
print(manual_zip([1, 2, 3], ["a", "b", "c", "d"]))