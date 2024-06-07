from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Card():
    def __init__(self,color,shape,filling,amount,location):
        self.color = color
        self.shape = shape
        self.filling = filling
        self.amount = amount
        self.location = location

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.color == other.color and
            self.shape == other.shape and
            self.filling == other.filling and
            self.amount == other.amount)
        else:
            return False