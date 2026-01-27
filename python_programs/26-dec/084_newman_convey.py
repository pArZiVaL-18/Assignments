def newman_convey(n):
    if n < 0: 
        return -1
    
    if n == 1 or n == 2:
        return 1
    
    ans = [0] * (n + 1)
    ans[1] = 1
    ans[2] = 1

    for i in range(3, n+1):
        ans[i] = ans[ans[i-1]] + ans[i - ans[i-1]]

    print(ans)
    return ans[n]


for i in range(10):
    print(newman_convey(i+5))