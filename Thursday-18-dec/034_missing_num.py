def find_missing_number(arr):
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    
    return len(arr) + 1

def find_missing_number_maths(arr):
    n = len(arr) + 1  
    
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum


def find_missing_number_xor(arr):
    n = len(arr) + 1
    
    xor_full = 0
    xor_arr = 0
    
    for i in range(1, n + 1):
        xor_full ^= i
    
    for num in arr:
        xor_arr ^= num
    
    return xor_full ^ xor_arr




print(find_missing_number([1, 2, 4, 5]))  
print(find_missing_number([2, 3, 4, 5]))  
print(find_missing_number_maths([1, 2, 4, 5]))  
print(find_missing_number_maths([2, 3, 4, 5]))
print(find_missing_number_xor([1, 2, 4, 5]))  
print(find_missing_number_xor([2, 3, 4, 5]))