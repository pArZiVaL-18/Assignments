import heapq

def find_largest_numbers(nums, k):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    largest = []
    for _ in range(k):
        largest.append(-heapq.heappop(max_heap))

    return largest

numbers = [12, 45, 3, 67, 23, 89, 5]
k = 5
print(find_largest_numbers(numbers, k))
