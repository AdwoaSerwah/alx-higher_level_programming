#!/usr/bin/python3
""" 1-main """
from models.base import Base


class Rectangle(Base):
    """Will write soon"""
    def to_dictionary(self):
        """Returns a dictionary"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of an object"""
        return self.width * self.height

    def display(self):
        """Displays the Rectangle with the # character"""
        [print() for _ in range(self.y)]
        [print(" " * self.x + "#" * self.width) for _ in range(self.height)]

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes of an object"""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)
