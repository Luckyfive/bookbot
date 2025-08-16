from stats import *
import sys

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():
    # path_to_file = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        # print(f"number of words: {word_count}")

        letter_dict = char_count(file_contents)
        # print(f"letter counter: {letter_dict}")

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        print()
        sorted_list = sorted(letter_dict, key=letter_dict.get, reverse=True)
        for key in sorted_list:
            print(f"{key}: {letter_dict[key]}")
        print("--- End report ---")
main()