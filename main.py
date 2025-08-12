from stats import *

def get_book_text(book_filepath):
    with open(book_filepath, 'r') as f:
        book_contents = f.read()
    return book_contents

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = num_words_in_book(book_text)
    print(f"{num_words} words found in the document")
    char_count = char_count_in_book(book_text)
    print(f"{char_count}")

main('./books/frankenstein.txt')