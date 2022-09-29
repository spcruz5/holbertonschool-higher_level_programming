#!/usr/bin/python3
""" is same class func"""


def is_same_class(obj, a_class):
    """ function that return True if object is exactly
    an instance of the specified class, otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
