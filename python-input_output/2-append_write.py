#!/usr/bin/python3
""" append file func"""


def append_write(filename="", text=""):
    """ write a file using `with` statement"""
    with open(filename, 'a') as file:
        r = file.write(text)
    return r
