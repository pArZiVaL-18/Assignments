import random

def get_random():
    return random.randint(1, 50)

def is_last_even(lst, p):
    
    lst.append(sum(lst) + 2)

    return lst[len(lst)-1] % 2 == 0

print(is_last_even([2, 3, 1, 4, 5, 7], 3))