from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from enum import Enum

import sys

WINHEIGHT = 400
WINWIDTH = 800

## CARDS:
# Each card has a colour, shape, shading and number
Attributes = Enum('Attributes', ['col', 'shape', 'shade', 'num'])

Color = Enum('Color', ['RED', 'GREEN', 'PURPLE'])
Shape = Enum('Shape', ['WAVE', 'DIAMOND', 'OVAL'])
Shading = Enum('Shading', ['EMPTY', 'LINED', 'FULL'])
#Number = Enum('Number', ['ONE', 'TWO', 'THREE'])

# card.attributes[col, shape, shade, num]

class Card:
    def __init__(self, col, shape, shade, num) :
        self.attributes = [col, shape, shade, num]

    # Three cards are a set unless some attribute is different in one card and equal in the two others.
    def is_set (self, one, two) :
        for i in Attributes :
            if self.attributes[i] != one.attributes[i] :
                if self.attributes[i] == two.attributes[i] or one.attributes[i] == two.attributes[i] :
                    return False
            elif self.attributes[i] != two.attributes[i] :
                return False
        return True


class MyWindow(QWidget) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel("ello"), 0, 0)

        grid.addWidget(QLabel("nee"), 1, 1)

        image1 = QLabel(self)
        pixmap = QPixmap("SetCards/RED1.png")
        image1.setPixmap(pixmap)
        grid.addWidget(image1, 0, 1)

        image2 = QLabel(self)
        pixmap2 = QPixmap("SetCards/RED2.png")
        image2.setPixmap(pixmap2)
        grid.addWidget(image2, 0, 5)


    def button1Clicked(self):
        self.label.setText("hellllll wat")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


window()
