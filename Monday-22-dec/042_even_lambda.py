def even_lambda(lst):
    return list(filter(lambda x: x%2==0, lst))


print(even_lambda([1, 2,3, 4,5, 6, 7, 8, 9]))