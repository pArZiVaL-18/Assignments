def get_kth_element(lst, k):
    if k < 0 or k > len(lst):
        print("Range out of bound. please input a valid index!")
    
    return lst[k]

print(get_kth_element([1, 2, 3, 4, 5, 6, 7, 9], 5))
