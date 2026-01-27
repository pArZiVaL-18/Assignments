import heapq
from collections import Counter

def top_k_elements(nums, k):
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if(len(heap) > k):
            heapq.heappop(heap)

    
    return heap

print(top_k_elements([1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5], 2))
