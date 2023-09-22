#!/usr/bin/python3

""" Square class inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """" Square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update attributes of Square"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
