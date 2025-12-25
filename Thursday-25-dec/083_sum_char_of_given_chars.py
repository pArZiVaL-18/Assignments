def find_char(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i]) - ord('a')

    sum = sum % 26
    return chr(sum + ord('a'))

print(find_char("zzz"))