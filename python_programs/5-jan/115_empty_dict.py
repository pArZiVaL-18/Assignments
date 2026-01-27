def is_all_empty(dict_list):
    for dict in dict_list:
        if dict:
            return False
        
    return True

dict_list = [{}, {}, {}]
dict_list2 = [{}, {"1": "roshant"}, {}]
print(is_all_empty(dict_list))
print(is_all_empty(dict_list2))