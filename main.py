from stats import num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = num_words(text)
    char_list = count_characters(text)
    print(f"Found {count_words} total words")
    print(f"found the following characters {char_list}")


main()