def get_all_divisors_sum(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

def is_amicable_pair(num1, num2):
    if num1 == num2:
        return False

    return get_all_divisors_sum(num1) == num2 and get_all_divisors_sum(num2) == num1


print(is_amicable_pair(220, 284))
print(is_amicable_pair(18, 21))