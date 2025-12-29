def count_odd(s):
    num = int(s) # not working
    count = 0
    while num != 0:
        if num & 1 == 1:
            count += 1
        num >>= 1
        print(num)
    
    return count


def count_odd_string(s):
    count = 0
    for i in range(len(s)):
        if s[len(s)-1] == '1':
            count += 1
        s = s[len(s)-1] + s[:len(s)-1]
        print(s)
    return count

print(count_odd_string("1011001101010"))