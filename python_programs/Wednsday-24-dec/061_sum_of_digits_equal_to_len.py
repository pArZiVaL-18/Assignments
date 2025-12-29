def sum_of_digits(n):
    sum = 0
    while(n > 0):
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def count(s):
    count = 0
    for i in range(0, len(s)):
        s2 = ''
        for j in range(i, len(s)):
            s2 = s2 + s[j]
            if(sum_of_digits(int(s2)) == len(s2)):
                count += 1
                # print(s2)
    return count



print(count("1123"))
print(count("123"))
print(count("111"))