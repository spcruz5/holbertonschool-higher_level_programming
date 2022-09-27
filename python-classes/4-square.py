#!/usr/bin/python3
class Square:
    __doc__ = "Square Validation"

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) == int:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                return self.__size
        else:
            raise TypeError("size must be an integer")