def get_max_diff(arr):
    max_sum = -1
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            max_sum = max((arr[i]-arr[j]), max_sum)
    return max_sum

print(get_max_diff([4, 3, 2, 1]))