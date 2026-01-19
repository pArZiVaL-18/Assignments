def run_length_encode(lst):
    if not lst:
        return []
    encoded = []
    current = lst[0]
    count = 1
    for item in lst[1:]:
        if item == current:
            count += 1
        else:
            encoded.append((current, count))
            current = item
            count = 1

    encoded.append((current, count))
    return encoded

lst = ["a", "a", "b", "b", "b", "c", "d", "d", "d", "d"]

print(run_length_encode(lst))