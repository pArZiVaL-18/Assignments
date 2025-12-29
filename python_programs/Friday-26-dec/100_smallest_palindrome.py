def is_palindrome(n):
    temp = str(n)
    return temp == temp[::-1]

def next_smallest_palindrome(n):
    found = 0
    ans = n
    while found != 1:
        if is_palindrome(ans+1):
            found = 1
        ans += 1
    
    return ans


print(next_smallest_palindrome(113))