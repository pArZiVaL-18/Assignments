def remove_digits(strings):
    cleaned_list = []
    
    for s in strings:
        cleaned = "".join(ch for ch in s if not ch.isdigit())
        cleaned_list.append(cleaned)
    
    return cleaned_list


print(remove_digits(["a1b2c3", "123abc", "no_digits_here", "4567"]))