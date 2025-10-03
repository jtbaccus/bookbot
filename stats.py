def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def word_counter(book_text):
    words = book_text.split()
    return len(words)

def character_counter(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict