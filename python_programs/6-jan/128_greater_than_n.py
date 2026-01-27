# Write a function to shortlist words that are longer than n from a given list of words.

def get_words(lst, n):
    ans = []
    for word in lst:
        if len(word) > n:
            ans.append(word)
    
    return ans


print(get_words(["roshan", "arin", "yuvraj", "prerana", "dhanesh"], 6))
