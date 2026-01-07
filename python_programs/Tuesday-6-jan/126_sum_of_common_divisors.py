def get_sum_of_common_divisors(num1, num2):
    n = min(num1, num2)
    sum = 0
    for i in range(2, n+1):
        if(num1 % i == 0 and num2 % i == 0):
            sum += i
        
    return sum

print(get_sum_of_common_divisors(6, 12))