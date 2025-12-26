from stats import num_words, count_characters, sort_on, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    count_words = num_words(text)
    char_list = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()