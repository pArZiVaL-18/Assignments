def sum_of_list_division(lst):
    sum = 0
    for element in lst:
        sum += element
    
    print(sum)
    return sum // len(lst)

print(sum_of_list_division([1, 2, 3, 4, 5, 10]))