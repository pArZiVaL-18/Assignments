def pow(a, b):
    power = abs(b)
    ans = a

    while(power > 1):
        ans = ans * a
        power -= 1
    
    return 1/ans if b < 0 else ans

print(pow(2, -3))
