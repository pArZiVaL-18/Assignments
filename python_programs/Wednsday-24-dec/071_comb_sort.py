def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr

print(comb_sort([1, 2, 3, 8, 7, 9, 6, 10, 1, -5]))


