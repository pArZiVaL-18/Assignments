def longest_word(lst):
    ans = len(lst[0])

    for item in lst:
        ans = max(ans, len(item))

    return ans

print(longest_word(["roshan", "pratik", "kartik", "chandrashekhar"]))