#!/usr/bin/python3
"""This module defines the function text_indentation"""


def text_indentation(text=""):
    """
    Print a text with two new lines after these characters: ., ?, :

    Args:
        text (str): Text to indent

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = (".", "?", ":")

    isNewline = False
    isSpace = False
    space = ""

    text = text.strip()
    for letter in text:
        if (letter == "\n" or letter in chars):
            isNewline = True
            # space = space + letter

        elif isNewline:
            if letter == " ":
                # isNewline = True
                isSpace = False
                continue
            else:
                isNewline = False
                space = ""

        elif letter == " ":
            isSpace = True
            space = space + letter
            continue

        if letter in chars:
            letter = letter + "\n\n"
        elif isSpace and letter != "\n" and letter != " ":
            letter = space + letter
            isSpace = False
            space = ""

        print(letter, end="")
