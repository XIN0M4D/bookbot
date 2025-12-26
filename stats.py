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

def sort_on(character_dictionary):
    return character_dictionary["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

     