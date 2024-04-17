#!/usr/bin/python3
"""function that read a text file and print it to stdout"""

def read_file(filename=""):
    """Read text file and print to stdout"""

    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
