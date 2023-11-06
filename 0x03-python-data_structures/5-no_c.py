#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            letter = ''
        new_string = new_string + letter
    return (new_string)
