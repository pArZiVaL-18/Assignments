def get_sum_between_range(arr, a, b):
    if a > len(arr) or b > len(arr):
        return -1
    sum = 0
    for i in range(a, b+1):
        sum += arr[i]
    return sum



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_sum_between_range(arr, 2, 5))
print(get_sum_between_range(arr, 1, 14))