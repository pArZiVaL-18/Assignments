def count_pairs_with_difference(arr, k):
    """
    Count all distinct pairs in the array that have a difference of k.

    Args:
        arr (list of int): Input array of integers
        k (int): Target difference

    Returns:
        int: Number of distinct pairs (a, b) such that |a - b| = k
    """
    numbers = set(arr)
    count = 0

    for num in numbers:
        if num + k in numbers:
            count += 1

    return count


arr = [1, 5, 3, 4, 2]
k = 2
print(count_pairs_with_difference(arr, k))  