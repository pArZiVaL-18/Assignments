import math
from collections import Counter

def product_of_non_repeated(tempList):
    prod=[i for i in tempList if tempList.count(i)==1]
    print(math.prod(prod))


def product_of_non_repeated_efficient(arr):
    freq = Counter(arr)
    return math.prod([x for x in arr if freq[x] == 1])


# Example usage
list_of_numbers = [1, 2, 3, 4, 1] 
product_of_non_repeated(list_of_numbers)
print(product_of_non_repeated_efficient(list_of_numbers))