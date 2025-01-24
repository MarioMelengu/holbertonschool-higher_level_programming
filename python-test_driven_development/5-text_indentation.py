#!/usr/bin/python3
"""Python program to add 2 integers"""


def text_indentation(text):

    """Function to print a text with two new lines after each '.', ':', or '?'.

        Args:
            text (str): text that is to be processed.

        Raises:
            TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', ':', '?']:
            # Skip any subsequent spaces after punctuation
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
            print("\n")
        i += 1
