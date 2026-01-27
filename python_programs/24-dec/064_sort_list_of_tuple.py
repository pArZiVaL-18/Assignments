def sort(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort([("roshan", 89), ("pratik", 87), ("priyanka", 98)]))