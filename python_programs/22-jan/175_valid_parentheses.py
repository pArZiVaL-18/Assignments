def is_valid_parenthese(s: str) -> bool:
    '''
    This functions takes a string of parenthese, and check whether the given sequence of parentheses are valid or not
    
    :param s: a string containing parentheses
    :type s: str
    :return: returns true of false whether the parenthese are valid or not
    :rtype: bool
    '''
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        if s[i] == ')':
            if count > 0:
                count -= 1
            else:
                return False
    
    return count == 0

print(is_valid_parenthese("()()(())"))
print(is_valid_parenthese("((())))"))