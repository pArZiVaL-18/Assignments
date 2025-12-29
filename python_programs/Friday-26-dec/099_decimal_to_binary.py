def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n < 0:
        print("Negative numbers not supported")

    ans = []
    while n > 0:
        ans.append(str(n % 2))
        n //= 2

    ans.reverse()
    return "".join(ans)


print(decimal_to_binary(17))
print(decimal_to_binary(-3))