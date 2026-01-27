def get_element(lst, index=0):
    ans = []
    for i in range(len(lst)):
        if len(lst[i]) > 1:
            ans.append(lst[i][index])

    return ans             

print(get_element([[1,2,3,4],[6,5,7,4],[8,9,0,2]], 2))
print(get_element([[1,2,3,4],[6,5,7,4],[8,9,0,2]]))