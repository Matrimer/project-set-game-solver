from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
import random

import sys

from Designe_SetSolver import *

WINHEIGHT = 400
WINWIDTH = 1500
class Location():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x == other.x and
            self.y == other.y)
        else:
            return False

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



class SetSolver():
    cardList = []
    foundSets = []
    def __init__(self):
        pass
    
#go through the card list and see if newCard is a duplicate of any card in the card list
    def noDuplicates(self, newCard):
        for card in enumerate(self.cardList):
            if(newCard==card):
                return False
        return True


    def addCardAndSolve(self,newCard):
        
        if(self.noDuplicates(newCard)):
            # Checks for sets with the new card and the cardlist then adds the card to the list
            for i,firstCard in enumerate(self.cardList):
                for secondCard in self.cardList[i+1:]:

                    if self.isSet(firstCard,secondCard,newCard):
                        self.foundSets.append([newCard.location,firstCard.location,secondCard.location])
            self.cardList.append(newCard)

    def isSet(self,one, two, three):
        # Loops over the fields/atributes of one whitch is an instance of a card
        # Not clean
        for attribute, value in one.__dict__.items():
            # compares cards bassed on there values at the atributes
            if getattr(one, attribute) != getattr(two, attribute):
                if getattr(three, attribute) in (getattr(one, attribute) , getattr(two, attribute)):
                    return False
            elif getattr(one, attribute) != getattr(three, attribute):
                return False
        return True 
    def getCard(self,location):
        # Returns a card from the cardlist based on the location
        for card in self.cardList:
            if card.location == location:
                return card
        return None
    def removeCard(self,location):
        # Removes a card from the cardlist based on the location
        card = self.getCard(location)
        if card is not None:
            self.cardList.remove(card)

class MyWindow(QWidget) :    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.setWindowIcon(QIcon("SetCards/RFW3.png"))
        self.initUI()

    def initUI(self):

        grid_layout = QGridLayout()

        # Set the layout for the main window
        self.setLayout(grid_layout)


        self.gridLayoutWidgetCardOptions = QtWidgets.QWidget(self)
        self.gridLayoutWidgetCardOptions.setGeometry(QtCore.QRect(450, 10, 700, 231))
        self.gridLayoutWidgetCardOptions.setObjectName("gridLayoutWidgetCardOptions")

        self.gridLayoutCardOptions = QtWidgets.QGridLayout(self.gridLayoutWidgetCardOptions)
        self.gridLayoutCardOptions.setObjectName("gridLayoutCardOptions")

        self.frame_4 = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        self.frame_4.setObjectName("frame_4")

        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 400, 200))


        self.horizontalLayoutWidgetCardOptions = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidgetCardOptions.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.horizontalLayoutWidgetCardOptions.setObjectName("horizontalLayoutWidgetCardOptions")
        self.horizontalLayoutCardOptions = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetCardOptions)
        self.horizontalLayoutCardOptions.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayoutCardOptions.setObjectName("horizontalLayoutCardOptions")
        self.labelShape = QtWidgets.QLabel(self.horizontalLayoutWidgetCardOptions)
        self.labelShape.setObjectName("labelShape")
        self.labelShape.setText("Shape:")
        self.horizontalLayoutCardOptions.addWidget(self.labelShape)

        self.radioButtonWave = QtWidgets.QRadioButton(self.horizontalLayoutWidgetCardOptions)
        self.radioButtonWave.setChecked(True)
        self.radioButtonWave.setAutoExclusive(True)
        self.radioButtonWave.setObjectName("radioButtonWave")
        self.radioButtonWave.setText("Wave")
        self.radioButtonWave.clicked.connect(self.UpdateCard)
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonWave)

        self.radioButtonOval = QtWidgets.QRadioButton(self.horizontalLayoutWidgetCardOptions)
        self.radioButtonOval.setAutoExclusive(True)
        self.radioButtonOval.setObjectName("radioButtonOval")
        self.radioButtonOval.setText("Oval")
        self.radioButtonOval.clicked.connect(self.UpdateCard)
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonOval)

        self.radioButtonDiamond = QtWidgets.QRadioButton(self.horizontalLayoutWidgetCardOptions)
        self.radioButtonDiamond.setAutoExclusive(True)
        self.radioButtonDiamond.setObjectName("radioButtonDiamond")
        self.radioButtonDiamond.setText("Diamond")
        self.radioButtonDiamond.clicked.connect(self.UpdateCard)
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonDiamond)

        self.gridLayoutCardOptions.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frameCardOptions = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        self.frameCardOptions.setObjectName("frameCardOptions")
        self.label = QtWidgets.QLabel(self.frameCardOptions)
        self.label.setGeometry(QtCore.QRect(0, 40, 35, 10))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidgetColor = QtWidgets.QWidget(self.frameCardOptions)
        self.horizontalLayoutWidgetColor.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.horizontalLayoutWidgetColor.setObjectName("horizontalLayoutWidgetColor")
        self.horizontalLayoutColor = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetColor)
        self.horizontalLayoutColor.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayoutColor.setObjectName("horizontalLayoutColor")
        self.labelColor = QtWidgets.QLabel(self.horizontalLayoutWidgetColor)
        self.labelColor.setObjectName("labelColor")
        self.labelColor.setText("Color:")
        self.horizontalLayoutColor.addWidget(self.labelColor)

        self.radioButtonRed = QtWidgets.QRadioButton(self.horizontalLayoutWidgetColor)
        self.radioButtonRed.setChecked(True)
        self.radioButtonRed.setAutoExclusive(True)
        self.radioButtonRed.setObjectName("radioButtonRed")
        self.radioButtonRed.setText("Red")
        self.radioButtonRed.clicked.connect(self.UpdateCard)
        self.horizontalLayoutColor.addWidget(self.radioButtonRed)

        self.radioButtonGreen = QtWidgets.QRadioButton(self.horizontalLayoutWidgetColor)
        self.radioButtonGreen.setAutoExclusive(True)
        self.radioButtonGreen.setObjectName("radioButtonGreen")
        self.radioButtonGreen.setText("Green")
        self.radioButtonGreen.clicked.connect(self.UpdateCard)
        self.horizontalLayoutColor.addWidget(self.radioButtonGreen)

        self.radioButtonPurple = QtWidgets.QRadioButton(self.horizontalLayoutWidgetColor)
        self.radioButtonPurple.setAutoExclusive(True)
        self.radioButtonPurple.setObjectName("radioButtonPurple")
        self.radioButtonPurple.setText("Purple")
        self.radioButtonPurple.clicked.connect(self.UpdateCard)
        self.horizontalLayoutColor.addWidget(self.radioButtonPurple)


        self.gridLayoutCardOptions.addWidget(self.frameCardOptions, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayoutWidget_Color = QtWidgets.QWidget(self.frame_6)
        self.horizontalLayoutWidget_Color.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.horizontalLayoutWidget_Color.setObjectName("horizontalLayoutWidget_Color")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_Color)
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelAmount = QtWidgets.QLabel(self.horizontalLayoutWidget_Color)
        self.labelAmount.setObjectName("labelAmount")
        self.labelAmount.setText("Amount:")
        self.horizontalLayout_4.addWidget(self.labelAmount)

        self.radioButtonColor1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_Color)
        self.radioButtonColor1.setChecked(True)
        self.radioButtonColor1.setAutoExclusive(True)
        self.radioButtonColor1.setObjectName("radioButtonColor1")
        self.radioButtonColor1.setText("1")
        self.radioButtonColor1.clicked.connect(self.UpdateCard)
        self.horizontalLayout_4.addWidget(self.radioButtonColor1)

        self.radioButtonColor2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_Color)
        self.radioButtonColor2.setAutoExclusive(True)
        self.radioButtonColor2.setObjectName("radioButtonColor2")
        self.radioButtonColor2.setText("2")
        self.radioButtonColor2.clicked.connect(self.UpdateCard)
        self.horizontalLayout_4.addWidget(self.radioButtonColor2)

        self.radioButtonColor3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_Color)
        self.radioButtonColor3.setAutoExclusive(True)
        self.radioButtonColor3.setObjectName("radioButtonColor3")
        self.radioButtonColor3.setText("3")
        self.radioButtonColor3.clicked.connect(self.UpdateCard)
        self.horizontalLayout_4.addWidget(self.radioButtonColor3)


        self.gridLayoutCardOptions.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelFilling = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.labelFilling.setObjectName("labelFilling")
        self.labelFilling.setText("Filling:")
        self.horizontalLayout_5.addWidget(self.labelFilling)

        self.radioButtonFull = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButtonFull.setChecked(True)
        self.radioButtonFull.setAutoExclusive(True)
        self.radioButtonFull.setObjectName("radioButtonFull")
        self.radioButtonFull.setText("Full")
        self.radioButtonFull.clicked.connect(self.UpdateCard)
        self.horizontalLayout_5.addWidget(self.radioButtonFull)

        self.radioButtonHalf = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButtonHalf.setAutoExclusive(True)
        self.radioButtonHalf.setObjectName("radioButtonHalf")
        self.radioButtonHalf.setText("Half")
        self.radioButtonHalf.clicked.connect(self.UpdateCard)
        self.horizontalLayout_5.addWidget(self.radioButtonHalf)

        self.radioButtonEmpty = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButtonEmpty.setAutoExclusive(True)
        self.radioButtonEmpty.setObjectName("radioButtonEmpty")
        self.radioButtonEmpty.setText("Empty")
        self.radioButtonEmpty.clicked.connect(self.UpdateCard)
        self.horizontalLayout_5.addWidget(self.radioButtonEmpty)

        self.gridLayoutCardOptions.addWidget(self.frame_7, 3, 0, 1, 1)
        self.NewCard = QtWidgets.QLabel(self.gridLayoutWidgetCardOptions)
        self.NewCard.setObjectName("NewCard")
        self.NewCard.setText("Image of user generated card")
        self.gridLayoutCardOptions.addWidget(self.NewCard, 0, 1, 3, 1)
        self.AddCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetCardOptions)
        self.AddCardButton.setObjectName("AddCardButton")
        self.AddCardButton.setText("Add Card")
        self.gridLayoutCardOptions.addWidget(self.AddCardButton, 1, 1, 3, 1)
        self.AddCardButton.clicked.connect(self.ChangeCard)  # Connect the clicked signal of the AddCardButton to the addCard method

        

        grid_layout.addWidget(self.gridLayoutWidgetCardOptions, 0, 15, 3, 4)  # Add the card options widget to the main layout and set its position to 2x2

        self.setLayout(grid_layout)  # Set the layout for the main window
        self.grid_layout = grid_layout
        # grid = QGridLayout()
        # self.setLayout(grid)

        # Create the grid layout
        

        # makes a 3 by 4 grid with random cards
        self.solver = SetSolver()
        
        for i in range(4):
            for j in range(3):
                # creates card based on i and j and random values and solves them and shows them
                location = Location(i,j)
                card = Card(random.choice(["purple","green","red"]),random.choice(["D","W","O"]),random.choice(["E","F","L"]),random.choice(["1","2","3"]),location)
                self.solver.addCardAndSolve(card)
                self.showCard(card,grid_layout)
    
        #Todo change name from set to something better because name set is python name
        for set in self.solver.foundSets:
            print(f"{set[0]} and {set[1]} and {set[2]}")

    def UpdateCard(self):
        # Updates the card in the card options widget
        color = ""
        shape = ""
        filling = ""
        amount = ""

        if self.radioButtonRed.isChecked():
            color = "Red"
        elif self.radioButtonGreen.isChecked():
            color = "Green"
        elif self.radioButtonPurple.isChecked():
            color = "Purple"

        if self.radioButtonWave.isChecked():
            shape = "W"
        elif self.radioButtonOval.isChecked():
            shape = "O"
        elif self.radioButtonDiamond.isChecked():
            shape = "D"

        if self.radioButtonFull.isChecked():
            filling = "F"
        elif self.radioButtonHalf.isChecked():
            filling = "L"
        elif self.radioButtonEmpty.isChecked():
            filling = "E"

        if self.radioButtonColor1.isChecked():
            amount = "1"
        elif self.radioButtonColor2.isChecked():
            amount = "2"
        elif self.radioButtonColor3.isChecked():
            amount = "3"
        image = QImage(f"SetCards/R{filling}{shape}{amount}.png")
        image = image.convertToFormat(QImage.Format.Format_RGB32)
        for i in range(image.width()):
            for j in range(image.height()):
                if image.pixelColor(i,j).black()==0:
                    image.setPixelColor(i,j,QColor(color))
        pixmap = QPixmap.fromImage(image)
        
        
        # self.gridLayoutCardOptions.addWidget(, 0,1,3,1)
        # print(card.color)
        # print(card.shape)
        # print(card.filling)
        # print(card.amount)
        # print(card.location)
        
        
        self.NewCard.setPixmap(pixmap)

    def showCard(self, card, grid_layout):
        self.addImage(grid_layout, f"SetCards/R{card.filling}{card.shape}{card.amount}.png", card.location.x, card.location.y, QColor(card.color))

    def ChangeCard(self):
        # Adds a card to the UI based on the selected options
        color = ""
        shape = ""
        filling = ""
        amount = ""

        if self.radioButtonRed.isChecked():
            color = "Red"
        elif self.radioButtonGreen.isChecked():
            color = "Green"
        elif self.radioButtonPurple.isChecked():
            color = "Purple"

        if self.radioButtonWave.isChecked():
            shape = "W"
        elif self.radioButtonOval.isChecked():
            shape = "O"
        elif self.radioButtonDiamond.isChecked():
            shape = "D"

        if self.radioButtonFull.isChecked():
            filling = "F"
        elif self.radioButtonHalf.isChecked():
            filling = "L"
        elif self.radioButtonEmpty.isChecked():
            filling = "E"

        if self.radioButtonColor1.isChecked():
            amount = "1"
        elif self.radioButtonColor2.isChecked():
            amount = "2"
        elif self.radioButtonColor3.isChecked():
            amount = "3"

        card = Card(color, shape, filling, amount, self.seletectedLocation)
        solver = SetSolver()
        solver.removeCard(self.seletectedLocation)
        solver.addCardAndSolve(card)
        self.showCard(card, self.grid_layout)
    
    def addImage(self, grid_layout, filelocation,x,y,color):
        # Creates and shows an image on the grid at x,y of file at filelocation with color color
        image = QImage(filelocation)
        image = image.convertToFormat(QImage.Format.Format_RGB32)
        for i in range(image.width()):
            for j in range(image.height()):
                if image.pixelColor(i,j).black()==0:
                    image.setPixelColor(i,j,color)
        pixmap = QPixmap.fromImage(image)
        button = QPushButton(self)
        button.setIcon(QIcon(pixmap))
        button.setIconSize(pixmap.size())
        button.clicked.connect(self.buttonClicked)
        # print(type(grid_layout))
        grid_layout.addWidget(button, x, y)
        # Remove widget at x, y from grid_layout

        # grid.addWidget(label, x, y)
    def buttonClicked(self):
        select_grid = self.gridLayoutWidgetCardOptions
        # Removes the clicked button from the grid
        button = self.sender()

        position = self.grid_layout.getItemPosition(self.grid_layout.indexOf(button))
        print(position)
        x = position[0]
        y = position[1]
        self.seletectedLocation = Location(x,y)
        card = self.solver.getCard(Location(x,y))

        if card is not None:
            #Creates and shows an image on the grid at x,y of file at filelocation with color color
            image = QImage(f"SetCards/R{card.filling}{card.shape}{card.amount}.png")
            image = image.convertToFormat(QImage.Format.Format_RGB32)
            for i in range(image.width()):
                for j in range(image.height()):
                    if image.pixelColor(i,j).black()==0:
                        image.setPixelColor(i,j,QColor(card.color))
            pixmap = QPixmap.fromImage(image)
            
            
            # self.gridLayoutCardOptions.addWidget(, 0,1,3,1)
            # print(card.color)
            # print(card.shape)
            # print(card.filling)
            # print(card.amount)
            # print(card.location)
            
            
            self.NewCard.setPixmap(pixmap)

            # self.gridLayoutCardOptions.addWidget(NewCard, 0, 1, 1, 1)
        else:
            print(f"Card not found at location {x},{y}")

        self.update()
    
    def update(self):
        self.label.adjustSize()

    

def window():
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()

    win = MyWindow()
    win.show()            
    # Old window

    sys.exit(app.exec())


window()

# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()dow()
# ui.setupUi(MainWindow)
# MainWindow.show()