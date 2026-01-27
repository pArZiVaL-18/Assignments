def count_even_xor_pairs_bruteforce(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) % 2 == 0:
                count += 1
    return count


def count_even_xor_pairs(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    even_pairs = even_count * (even_count - 1) // 2
    odd_pairs = odd_count * (odd_count - 1) // 2

    return even_pairs + odd_pairs


arr = [1, 2, 3, 4, 5, 6]

print("Efficient:", count_even_xor_pairs(arr))  
print("Brute-force:", count_even_xor_pairs_bruteforce(arr))  

