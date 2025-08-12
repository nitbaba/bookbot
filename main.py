from stats import *

def get_book_text(book_filepath):
    with open(book_filepath, 'r') as f:
        book_contents = f.read()
    return book_contents

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = num_words_in_book(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_list = sort_char_counts(char_count_in_book(book_text))
    for item in sorted_list:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

main('./books/frankenstein.txt')