from stats import count_book_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():

    #checks if sys.argv has two entries, and exits the program if not
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #book_location = "books/frankenstein.txt"
    number_of_words = count_book_words(get_book_text(sys.argv[1]))
    #print(f"Found {number_of_words} total words")
    number_of_char = count_characters(get_book_text(sys.argv[1]))
    #print(number_of_char)

    #test
    sorted_list = sort_dict(number_of_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for d_item in sorted_list:
        if d_item["char"].isalpha():
            print(f"{d_item["char"]}: {d_item["num"]}")


main()