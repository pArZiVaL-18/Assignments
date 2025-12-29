def nearest_small(lst, n):
    nearest = None

    for item in lst:
        if item < n:
            if nearest is None or item > nearest:
                nearest = item

    return nearest if nearest is not None else -1



print(nearest_small([3, 5, 7, 5, 1 ], 2))