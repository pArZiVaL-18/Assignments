def decimal_to_binary(n):
    ans = []
    while n > 0:
        ans.append(n % 2)
        n //= 2

    return int(''.join(str(n) for n in ans[::-1]))

n = int(input("Enter number to convert : "))
print(decimal_to_binary(n))