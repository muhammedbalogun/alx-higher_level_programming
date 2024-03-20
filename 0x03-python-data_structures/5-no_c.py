#!/usr/bin/python3
def no_c(my_string):
    char = ["c", "C"]
    for letter in char:
        if letter in my_string:
            new_str = my_string.translate({ord(letter): None})
    return new_str
