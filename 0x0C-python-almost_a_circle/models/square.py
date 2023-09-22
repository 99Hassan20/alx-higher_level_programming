#!/usr/bin/python3

""" Square class inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """" Square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the square class"""
        super().__init__(size, size, x, y, id)()

    def __str__(self):
        """ Return string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
