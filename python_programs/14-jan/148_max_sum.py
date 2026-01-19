def max_sum_split(n):
    digits = sorted(str(n), reverse=True)
    num1, num2 = "", ""
    for i, d in enumerate(digits):
        if i % 2 == 0:
            num1 += d
        else:
            num2 += d

    return int(num1), int(num2), int(num1) + int(num2)


print(max_sum_split(9876))