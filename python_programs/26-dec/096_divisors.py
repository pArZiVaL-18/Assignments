def get_all_divisors(n):
    ans = []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)

    return ans

print(get_all_divisors(18))