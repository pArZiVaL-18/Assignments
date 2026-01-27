def get_sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            sum += abs(arr[i] - arr[j])
        
    return sum

print(get_sum([4, 3, 2, 1])) 
# 1, 2, 3, 1, 2, 1