def single_element(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    for i in range(0, n - 1, 2):
        if arr[i] != arr[i + 1]:
            return arr[i]
    return arr[-1]

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6 ]
print(single_element(arr))
