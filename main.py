# define the main function. It needs to define the file location,
# get the book text from that file location,
# and print the number of words in it.
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = word_count(text)
    characters = character_count(text)
    characters_list = dict_list(characters)
    print(f"This document contains {words} words.")
    for i in characters_list:
        character = i["character"]
        count = i["count"]
        print(f"The letter {character} appears {count} times.")

# define the function that gets the book text from the file location (the latter is the single argument).
def get_book_text(path):
    with open(path) as f:   # use f as the shorthand for the file, when opened, in the file location "path"...
        return f.read()     # ... read f, and return its contents

# define a function that splits the text into a list of elements based on whitespace, and returns the number of elements in the list.
def word_count(text):
    words = text.split()
    return len(words)

# define a function that first turns all characters in the text to lower case, and then counts every character instance.
def character_count(text):
    lowered_text = text.lower()     # set the whole text to lower case
    characters_dict = {}            # create an empty list for the characters
    for character in lowered_text:  # for every character: if it's already in the dict, increase value by 1, else create with value 1
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

# define another function that converts the dictionary into a list of dictionaries, and sorts the list based on count
def dict_list(dict):
    dict_list = []
    for i in dict:
        if i.isalpha():     # only add characters that are alphabetic
            dict_list.append({"character": i, "count": dict[i]})
    sorted_list = sorted(dict_list, key=lambda x: x["count"], reverse=True)
    return sorted_list

# at the end of the script, run the main function 
main()