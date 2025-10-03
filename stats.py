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

'''Chat GPTs initial suggestion:

def sort_characters(char_dict):
    # Convert dictionary into a list of {"char": c, "num": n}
    char_list = []
    for c, n in char_dict.items():
        if c.isalpha():   # only include letters
            char_list.append({"char": c, "num": n})

    # Sort the list by "num" descending
    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list '''

# My rookie attempt after Chat GPT walked me through the cleaner way above

def sort_on(item):
    return item["num"]

def sort_characters(char_dict):
    # Convert dictionary into a list of {"char": c, "num": n}
    char_list = []
    for c, n in char_dict.items():
        if c.isalpha():   # only include letters
            char_list.append({"char": c, "num": n})

    # Sort the list by "num" descending
    char_list.sort(key=sort_on, reverse=True)

    return char_list
