#!/usr/bin/python3
"""[summary]"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns:
            [type]: [description]
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """
        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """[summary]
        """
        atr = ['id', 'size', 'x', 'y']

        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        for i, v in enumerate(args[:4]):
            setattr(self, atr[i], v)

    def to_dictionary(self):
        """
        Returns:
            [type]: [description]
        """
        dict_ = {'id': self.id, 'size': self.size,
                 'x': self.x, 'y': self.y}
        return dict_
