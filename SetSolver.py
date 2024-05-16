from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
import random

import sys

WINHEIGHT = 400
WINWIDTH = 800


class MyWindow(QWidget) :    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        # makes a 3 by 4 grid with random red cards
        for i in range(3):
            for j in range(4):
                self.addImage(grid,f"SetCards/R{random.choice(["E","F","L"])}{random.choice(["D","W","O"])}{random.choice(["1","2","3"])}.png",i,j)

        # grid.addWidget(QLabel("ello"), 0, 0)

        # grid.addWidget(QLabel("nee"), 1, 1)

        
        
    def addImage(self, grid, filelocation,x,y):
        image = QLabel(self)
        pixmap = QPixmap(filelocation)
        image.setPixmap(pixmap)
        grid.addWidget(image, x, y)
    
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