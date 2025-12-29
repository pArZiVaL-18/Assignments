def find_missing_ranges(nums, start, end):
    nums = sorted(nums)
    missing = []

    prev = start - 1

    for num in nums:
        if num > prev + 1:
            missing.append((prev + 1, num - 1))
        prev = num

    if prev < end:
        missing.append((prev + 1, end))

    return missing


print(find_missing_ranges([2, 3, 7, 8, 10, 11], 1, 20))