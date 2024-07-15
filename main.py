# define the main function. It needs to define the file location,
# get the book text from that file location,
# and print the number of words in it.
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = word_count(text)
    print(f"This document contains {words} words.")

# define the function that gets the book text from the file location (the latter is the single argument).
def get_book_text(path):
    with open(path) as f:   # use f as the shorthand for the file, when opened, in the file location "path"...
        return f.read()     # ... read f, and return its contents

# define a function that splits the text into a list of elements based on whitespace, and returns the number of elements in the list.
def word_count(text):
    words = text.split()
    return len(words)

# at the end of the script, run the main function 
main()