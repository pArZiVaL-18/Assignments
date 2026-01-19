def remove_elements(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]

print(remove_elements(list1, list2))  
