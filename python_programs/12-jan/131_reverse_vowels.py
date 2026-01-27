def is_vowel(ch):
    return ch in "aeiouAEIOU"

def reverse_vowels(s):
    s = list(s)
    n = len(s)

    left = 0
    right = n - 1

    while left < right:
        while left < right and not is_vowel(s[left]):
              left += 1
        
        while right > left and not is_vowel(s[right]):
              right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return "".join(s)


print(reverse_vowels("programming"))