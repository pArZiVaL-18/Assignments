def is_monotonic(arr):
    if len(arr) <= 2:
        return True

    increasing = True
    decreasing = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False

    return increasing or decreasing


print(is_monotonic([1, 2, 2, 3]))   
print(is_monotonic([5, 4, 4, 1]))   
print(is_monotonic([1, 3, 2]))     
