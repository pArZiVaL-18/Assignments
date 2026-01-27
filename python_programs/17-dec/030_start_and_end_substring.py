# from collections import Counter

# def count_same_start_end_substrings(s):
#     freq = Counter(s)
#     count = 0

#     for n in freq.values():
#         count += n * (n + 1) // 2

#     return count


# s1 = "abcab"
# result1 = count_same_start_end_substrings(s1)
# print(f"Number of substrings in '{s1}' that start and end with the same character: {result1}")

def count_same_start_end_sub(s):
    n = len(s)
    ans=[]

    for i in range(n):
        for j in range(i+1, n+1):
            word = s[i:j]
            if(word[0] == word[-1]):
                ans.append(word)
        

    return ans

print(count_same_start_end_sub("aba"))