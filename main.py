import sys
from stats import get_book_text, word_counter, character_counter, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)

    # Word count
    num_words = word_counter(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    char_counts = character_counter(book_text)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
