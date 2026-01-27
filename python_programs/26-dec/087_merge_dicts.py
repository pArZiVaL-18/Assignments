def merge_dicts(d1, d2, d3):
    return {**d1, **d2, **d3}


# ** is a spread operator for key:value pair data like dict
# when used within {} or in a function call it works like spread operator 
# other time it works as a power operator

# * is similar to ** but works for sequencial data like list, tuple etc.

print(merge_dicts({"a": 1, "b": 3}, {"c": 2, "b": 2}, {"d": 5, "c":4}))