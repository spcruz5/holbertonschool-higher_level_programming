#!/usr/bin/python3
""" Class base"""
from models.base import Base


class Rectangle(Base):
        """ Rectangle class"""
        def __init__(self, width, height, x=0, y=0, id=None):
                """ function that defines the variables"""
                self.__id = super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        @property
        def width(self):
                """ Function that get the width
                Return:
                        private attribute width
                """
                return self.__width

        @property
        def height(self):
                """ Function that get the height
                Return:
                        private attribute height
                """
                return self.__height
                      
        @property
        def x(self):
                """ getter method of x"""
                return self.__x

        @property
        def y(self):
                """ getter method of y"""
                return self.__y

        @width.setter
        def width(self, value):
                """ setter method of width"""
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value <= 0:
                        raise ValueError("width must be > 0")
                self.__width = value

        @height.setter
        def height(self, value):
                """ setter method of height"""
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value <= 0:
                        raise ValueError("height must be > 0")
                self.__height = value

        @x.setter
        def x(self, value):
                """ setter method of x"""
                if type(value) is not int:
                        raise TypeError("x must be an integer")
                if value < 0:
                        raise ValueError("x must be >= 0")
                self.__x = value

        @y.setter
        def y(self, value):
                """ setter method of y"""
                if type(value) is not int:
                        raise TypeError("y must be an integer")
                if value < 0:
                        raise ValueError("y must be >= 0")
                self.__y = value
 
        def area(self):
                """ return the area of the rectangle"""
                return self.__height * self.__width

        def display(self):
                """ print in stdout the Rectangle"""
                w = self.__width
                h = self.__height
                x = self.__x
                y = self.__y
                for i in range(y):
                        print("")
                for i in range(h):
                        for i in range(x):
                                print("", end=" ")
                        for i in range(w):
                                print('#', end="")
                        print("")
