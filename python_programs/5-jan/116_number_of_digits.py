def tuple_to_integer(tup):
    number = 0
    for n in tup:
        number = number * 10 + n

    return number

tup = (4, 3, 5, 2, 6, 1)
print(tuple_to_integer(tup))