def values_greater_than(lst, threshold):
    """
    Find all values in a list that are greater than a specified number.

    Args:
        lst (list of numbers): The list of numeric values to check.
        threshold (number): The number to compare against.

    Returns:
        list: A list of values from lst that are greater than threshold.
    """
    return [x for x in lst if x > threshold]


numbers = [4, 7, 1, 9, 3]
threshold = 5

print(values_greater_than(numbers, threshold))
