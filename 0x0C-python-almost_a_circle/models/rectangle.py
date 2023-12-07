#!/usr/bin/python3
"""
My rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """My rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

    @property
    def width(self):
        """
My rectangle class
"""

        return self.__width

    @width.setter
    def width(self, value):
        """
My rectangle class
"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
My rectangle class
"""

        return self.__height

    @height.setter
    def height(self, value):
        """
My rectangle class
"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
My rectangle class
"""

        return self.__x

    @x.setter
    def x(self, value):
        """
My rectangle class
"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
My rectangle class
"""

        return self.__y

    @y.setter
    def y(self, value):
        """
My rectangle class
"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
My rectangle class
"""

        return self.__width * self.__height

    def display(self):
        """
My rectangle class
"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            num = " " * self.x
            hashh = "#" * self.__width
            print(f"{num}{hashh}")

    def __str__(self):
        """
My rectangle class
"""
        hei = self.__height
        wi = self.__width
        return f"[Rectangle] ({self.id}) {self.x}/{self.__y} - {wi}/{hei}"

    def update(self, *args, **kwargs):
        """
My rectangle class
"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """
My rectangle class
"""

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
