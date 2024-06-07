from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys

from SetSolver import *
from MyWindow import *
from DuplicateDialog import *
from Card import *
from Location import *

def main():
    solver = SetSolver()
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


