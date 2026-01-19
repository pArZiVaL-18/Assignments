def count_alphabet_position_matches(s):
    count = 0
    for index, char in enumerate(s):
        if char.isalpha():
            pos = ord(char.lower()) - ord('a') + 1
            if pos == index + 1:
                count += 1
    return count

print(count_alphabet_position_matches("Abc"))       # 3
print(count_alphabet_position_matches("aBcD"))      # 4
print(count_alphabet_position_matches("HecdloWorld")) # 0
