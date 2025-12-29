def even_odd_division(lst):
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            odd = lst[i]
            break

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even = lst[i]
            break

    print( even , odd)
    return even/odd

print(even_odd_division([3, 10, 8, 2, 5, 9]))