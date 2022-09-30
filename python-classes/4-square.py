#!/usr/bin/python3
""" This is class named Square that defines a square """


class Square:
        """ definition """
        def __init__(self, size=0):
                """ Definition of private instance attribute size
                which is asigned with the double underscore before the name
                Args:
                    size (int): private instance attribute.
                Raises:
                    TypeError: if `size` is not an integer
                    ValueError: if `size` is less than zero
                """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                elif size < 0:
                        raise ValueError("size must be >=0")
                else:
                        self.__size = size

        @property
        def size(self):
                """ getter function"""
                return self.__size

        @size.setter
        def size(self, value):
                """ setter func """
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                elif value < 0:
                        raise ValueError("size must be >=0")
                else:
                        self.__size = value

        def area(self):
                """ Definition of function area that calculate
                the area of the square"""
                return self.__size ** 2
