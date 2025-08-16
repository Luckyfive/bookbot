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