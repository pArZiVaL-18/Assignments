def sort_sublists(lst):
    return list(map(lambda x: sorted(x), lst))


print(sort_sublists([["roshan", "pratik"],["girish", "rohit"], ["priyanka", "kajal"]]))