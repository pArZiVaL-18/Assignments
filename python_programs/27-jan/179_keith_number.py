def is_keith_number(n):
    """
    Check whether a given number is a Keith number.

    A Keith number is a number that appears in a sequence generated
    from its own digits. The sequence starts with the digits of the
    number, and each subsequent term is the sum of the previous
    k terms, where k is the number of digits in the original number.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is a Keith number, False otherwise.
    """
    digits = [int(d) for d in str(n)]
    k = len(digits)
    seq = digits.copy()

    while True:
        next_term = sum(seq[-k:])
        if next_term == n:
            return True
        if next_term > n:
            return False
        seq.append(next_term)


print(is_keith_number(197))
print(is_keith_number(742))   
print(is_keith_number(19))    
