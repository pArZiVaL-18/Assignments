from math import gcd

def find_pair_with_lcm_in_range(
    nums: list,
    low: int,
    high: int
) -> tuple:
    """
    Finds two distinct numbers in nums such that their LCM
    lies within the inclusive range [low, high].

    Parameters:
        nums (list): List of positive integers
        low (int): Lower bound of the LCM range
        high (int): Upper bound of the LCM range

    Returns:
        tuple[int, int]: A valid pair (a, b) if found
        None: If no such pair exists
    """

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            a = nums[i]
            b = nums[j]

            current_lcm = (a * b) // gcd(a, b)

            if low <= current_lcm <= high:
                return a, b

    return None

nums = [4, 6, 8, 12]
low = 20
high = 30

result = find_pair_with_lcm_in_range(nums, low, high)
print(result) 
