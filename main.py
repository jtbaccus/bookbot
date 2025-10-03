from stats import get_book_text
from stats import word_counter
from stats import character_counter

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_text)
    print(f"Found {num_words} total words")
    
    char_counts = character_counter(book_text)
    print(char_counts)


if __name__ == "__main__":
    main()