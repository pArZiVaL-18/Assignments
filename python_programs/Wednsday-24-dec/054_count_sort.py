def count_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)

    cntArr = [0] * (maxval + 1)

    for v in arr:
        cntArr[v] += 1

    for i in range(1, maxval + 1):
        cntArr[i] += cntArr[i - 1]

    ans = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans

print(count_sort([1, 5, 3, 2, 3, 3, 2, 1, 5]))