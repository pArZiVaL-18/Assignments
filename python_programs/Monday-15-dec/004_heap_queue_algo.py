# import heapq

# def find_largest_numbers(nums, k):
#     max_heap = [-num for num in nums]
#     heapq.heapify(max_heap)

#     largest = []
#     for _ in range(k):
#         largest.append(-heapq.heappop(max_heap))

#     return largest

# numbers = [12, 45, 3, 67, 23, 89, 5]
# k = 5
# print(find_largest_numbers(numbers, k))


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


heap = MaxHeap()

nums = [12, 3, 45, 7, 19, 26]
for num in nums:
    heap.insert(num)

print("Largest element:", heap.extract_max())

