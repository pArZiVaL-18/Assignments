def first_last_occurrence(s, char):# function to remove first and last occurrence of char
    first_index = s.find(char)
    last_index = s.rfind(char)

    if first_index == -1:
        return s
    
    if first_index == last_index:
        return s[:first_index] + s[first_index + 1:]

    modified_string = s[:first_index] + s[first_index + 1: last_index] + s[last_index + 1:] 
    return modified_string




def keep_first_last_only(s, char):# function to keep only the first and last occurrence of char
    first = s.find(char)
    last = s.rfind(char)

    if first == -1 or first == last:
        return s
    
    mid = s[first+1 : last].replace(char, '')
    return s[:first + 1] + mid + s[last:]



print(keep_first_last_only("abaasca", "a"))  # Output: "aa"
print(keep_first_last_only("abcdefabcabcabcabc", "a"))  # Output: "d"