#!/usr/bin/python3
""" Define a square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        if self.__size <= 0:
            print("")
        else:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end='')
                print("")