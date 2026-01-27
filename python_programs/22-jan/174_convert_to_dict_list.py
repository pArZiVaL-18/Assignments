def dict_of_lists(lst: list) -> dict:
    '''
    Returns: a dictionary containing unique keys and list of values

    params: a list of key value pair
    '''
    result = {}

    for key, value in lst:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    
    return result

print(dict_of_lists([(1, 3), (2, 4), (1, 5), (2, 7), (3, 1)]))
