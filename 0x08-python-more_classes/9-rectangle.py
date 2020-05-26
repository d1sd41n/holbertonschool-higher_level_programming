#!/usr/bin/python3
"""[summary]"""


class Rectangle:
    """[summary]
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Arguments:
            value {[type]} -- [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__width * self.__height

    def perimeter(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            w = self.__width
            h = self.__height
            d = str(self.print_symbol)
            r = ""
            r = "\n".join(d * w for i in range(h))
            return r

    def __repr__(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """[summary]
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """[summary]

        Arguments:
            rect_1 {[type]} -- [description]
            rect_2 {[type]} -- [description]

        Raises:
            TypeError: [description]
            TypeError: [description]

        Returns:
            [type] -- [description]
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def perimeter(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @classmethod
    def square(cls, size=0):
        """[summary]

        Keyword Arguments:
            size {int} -- [description] (default: {0})

        Returns:
            [type] -- [description]
        """
        return cls(size, size)
