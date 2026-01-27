def remove_everythink_except_alphanumric(s):
    ans = []
    for i in range(0, len(s)):
        if s[i].isalnum():
            ans.append(s[i])
        
    return "".join(ans)

print(remove_everythink_except_alphanumric("Hello, World! 123 @Python$"))