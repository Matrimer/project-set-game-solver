from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys

WINHEIGHT = 400
WINWIDTH = 800


class MyWindow(QMainWindow) :
    def __init__(self) :
        super(MyWindow, self).__init__()
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.initUI()

    
    def initUI(self):
        
        self.label = QtWidgets.QLabel("test",self)
        self.label.setText("test settext")
        self.label.move(50, 50)

        self.button1 = QPushButton("click me?", self)
        self.button1.clicked.connect(self.button1Clicked)

    def button1Clicked(self):
        self.label.setText("test clickedddd button 1?")
        self.update()
    
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()