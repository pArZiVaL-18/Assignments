# Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

def get_diff(s):
    if not s:
        return 0
    ones = s.count("1")
    return (len(s) - ones) - ones

def get_max_diff(s):
    max_diff = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            # print(s[i:j])
            max_diff = max(get_diff(s[i:j]), max_diff)
    return max_diff
        

print(get_diff("00001"))
print(get_max_diff("000111"))
    