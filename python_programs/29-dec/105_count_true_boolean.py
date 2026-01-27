def count_true_boolean(lst):
    return len([x for x in lst if x == True])


print(count_true_boolean([True, False, True, True, False]))