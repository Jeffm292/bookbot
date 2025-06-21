import sys
# stats.py
def get_num_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    character = {}
    for char in text:
        if char.lower() in character:
            character[char.lower()] += 1
        else:
            character[char.lower()] = 1
    return character


def dict_sort(character):
    result = []
    for key, value in character.items():
        if key.isalpha():
            result.append({"char": key, "num": value})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result
