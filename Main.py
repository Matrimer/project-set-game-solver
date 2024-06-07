import sys

from SetSolver import *
from MyWindow import *
from DuplicateDialog import *
from Card import *
from Location import *

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


