def sum_diff(n):
    n = abs(n)
    even_sum = 0
    odd_sum = 0

    flag = 1
    while n != 0:
        if flag == 1:
            odd_sum += n % 10
            flag = 0
        else:
            even_sum += n % 10
            flag = 1
        n //= 10
    print(even_sum, odd_sum)
    return even_sum - odd_sum

print(sum_diff(-121212121))
