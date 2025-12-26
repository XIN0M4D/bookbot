def num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    unique_characters = {}
    for ch in text:
        lowered = ch.lower()
        if lowered in unique_characters:
            unique_characters[lowered] += 1
        else:
            unique_characters[lowered] = 1
    return unique_characters