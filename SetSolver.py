from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 

import sys

WINHEIGHT = 400
WINWIDTH = 800

class DragButton(QPushButton):

    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)

class MyWindow(QWidget) :    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.initUI()
        self.setAcceptDrops(True)
    

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel("ello"), 0, 0)

        grid.addWidget(QLabel("nee"), 1, 1)

        image1 = QLabel(self)
        pixmap = QPixmap("settest01.png")
        image1.setPixmap(pixmap)
        grid.addWidget(image1, 0, 1)

        image2 = QLabel(self)
        pixmap2 = QPixmap("settest01.png")
        image2.setPixmap(pixmap2)
        grid.addWidget(image2, 0, 5)

        button1 = DragButton("A")
        grid.addWidget(button1)

        button2 = DragButton("B")
        grid.addWidget(button2)
        
    def dragEnterEvent(self, e):
        e.accept()
        
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