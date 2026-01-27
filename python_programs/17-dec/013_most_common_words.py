def most_common_words(word_dict):
    if not word_dict:
        return []

    max_count = max(word_dict.values())
    return [word for word, count in word_dict.items() if count == max_count]


words = {
    "apple": 4,
    "banana": 5,
    "orange": 5,
    "grape": 2
}

print(most_common_words(words))
