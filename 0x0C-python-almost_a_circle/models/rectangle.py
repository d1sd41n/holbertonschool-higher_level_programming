#!/usr/bin/python3
"""[summary]"""
from models.base import Base


class Rectangle(Base):
    """[summary]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns:
            [type]: [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value ([type]): [description]
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Returns:
            [type]: [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value ([type]): [description]
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Returns:
            [type]: [description]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Args:
            value ([type]): [description]
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Returns:
            [type]: [description]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Args:
            value ([type]): [description]
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Returns:
            [type]: [description]
        """
        return self.width * self.height

    def display(self):
        """[summary]
        """
        board = ""
        for i in range(self.y):
            board += '\n'
        for j in range(self.height):
            board += ' ' * self.x + '#' * self.width + '\n'
        print(board, end='')

    def __str__(self):
        """
        Returns:
            [type]: [description]
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        """[summary]
        """
        atr = ['id', 'width', 'height', 'x', 'y']

        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        for i, v in enumerate(args[:5]):
            setattr(self, atr[i], v)

    def to_dictionary(self):
        """
        Returns:
            [type]: [description]
        """
        dict_ = {'id': self.id, 'width': self.width,
                 'height': self.height, 'x': self.x,
                 'y': self.y
                 }
        return dict_
