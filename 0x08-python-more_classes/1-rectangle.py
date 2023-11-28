#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    @property
    def width(self):
        return self.__width


    @property
    def height(self):
        return self.__height


    @width.setter
    def width(self, value: int):
        try:
            if not value.isdigit():
                raise TypeError
            if value < 0:
                raise ValueError
            self.__width = value
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")


    @height.setter
    def height(self, value: int):
        try:
            if not value.isdigit():
                raise TypeError
            if value < 0:
                raise ValueError
            self.__height = value
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
