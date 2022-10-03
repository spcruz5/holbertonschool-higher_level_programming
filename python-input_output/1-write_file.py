#!/usr/bin/python3
""" write file func"""


def write_file(filename="", text=""):
    """ write a file using `with` statement"""
    with open(filename, 'w') as file:
        r = file.write(text)
    return
