
def find_count_of_each_digit(number):
    digit_count = {str(digit): 0 for digit in range(10)}

    for digit in str(number):
        if digit in digit_count:
            digit_count[digit] += 1

    return digit_count

print(find_count_of_each_digit(12345678901234567890))

result = find_count_of_each_digit(12034022)

for key in reversed(result):
    print(key, result[key])
