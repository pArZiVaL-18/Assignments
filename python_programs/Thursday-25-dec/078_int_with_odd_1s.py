# string approach
def odd_no_of_ones(lst):
    ans = []
    for item in lst:
        if bin(item).count("1") % 2 != 0:
            ans.append(item)
        
    return ans

# bit manipulation approach
def odd_no_of_ones_bit_manipulation(lst):
    ans = []
    for element in lst:
        count = 0
        item = element
        while element != 0:
            if element & 1 == 1:
                count += 1
            element = element >> 1
        
        if count % 2 != 0:
            ans.append(item)
    return ans



print(odd_no_of_ones([1, 2, 3, 4, 6, 7, 8]))
print(odd_no_of_ones_bit_manipulation([1, 2, 3, 4, 6, 7, 8]))


