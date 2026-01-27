
def flip(arr, n):
    start = 0
    end = n
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# print(flip([4, 3, 2, 1], 3))


def get_max_index(arr, n):
    max_element = arr[0]
    max_idx = 0
    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]

            max_idx = i

    return max_idx

# print(get_max_index([4, 3, 5, 2, 10], 5))

def pancake_sort(arr):
    curr = len(arr)-1
    while curr > 0:
        max_idx = get_max_index(arr, curr)

        if(max_idx != curr):
            flip(arr, max_idx)

            flip(arr, curr)
        curr -= 1
    
    return arr


arr= [7, 6, 8, 5, 9, 4, 0, 3, 2, -4]
print(pancake_sort([5, 4, 6, 2, 8, 1, 9, 3]))
print(pancake_sort(arr))