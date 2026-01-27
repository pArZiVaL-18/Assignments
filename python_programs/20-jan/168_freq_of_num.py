def get_freq(arr, n):
    freq = 0
    for element in arr:
        if element == n:
            freq += 1
    
    return freq

arr = [3, 4, 2, 4, 5, 3, 3, 6, 7, 3, 2, 4, 3, 4]
print("Frequency of 3 : ",get_freq(arr, 3))
print("Frequency of 4 : ",get_freq(arr, 4))