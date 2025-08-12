def num_words_in_book(book):
    book_as_list = book.split()
    return len(book_as_list)

def char_count_in_book(book):
    char_dict = {}
    lower = book.lower()
    for char in lower:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict