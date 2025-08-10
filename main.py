def get_book_text(book_filepath):
    with open(book_filepath, 'r') as f:
        book_contents = f.read()
    return book_contents

def num_words_in_book(book):
    book_as_list = book.split()
    return len(book_as_list)

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = num_words_in_book(book_text)
    print(f"{num_words} words found in the document")

main('./books/frankenstein.txt')