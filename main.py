from stats import num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = num_words(text)
    print(f"Found {count_words} total words")



main()