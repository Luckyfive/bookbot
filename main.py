def count_words(given_string):
    str_list = given_string.split()
    word_count = len(str_list)
    return word_count

def char_count(given_string):   
    letter_dict = {}
    for letter in given_string:
        curr_letter = str.lower(letter)
        if curr_letter not in letter_dict:
            letter_dict[curr_letter] = 1
        else:
            letter_dict[curr_letter] += 1
    
    return letter_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        # print(f"number of words: {word_count}")

        letter_dict = char_count(file_contents)
        # print(f"letter counter: {letter_dict}")

        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document")
        print()
        sorted_list = sorted(letter_dict, key=letter_dict.get, reverse=True)
        for key in sorted_list:
            print(f"The '{key}' character was found {letter_dict[key]} times")
        print("--- End report ---")
main()