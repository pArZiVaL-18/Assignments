def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a

def gcd_of_array(lst):
    ans = gcd(lst[0], lst[1])
    for i in range(2, len(lst)):
        ans = gcd(ans, lst[i])

    return ans

print(gcd_of_array([12, 40, 36]))
