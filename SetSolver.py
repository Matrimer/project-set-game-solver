from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import random

import sys

from Designe_SetSolver import *

WINWIDTH = 1500
WINHEIGHT = 400

DIALOGWIDTH = 900
DIALOGHEIGHT = 200


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Duplicate card")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("You are adding a duplicate")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

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
    def Duplicates(self, newCard):
        for card in self.cardList:
            if newCard == card:
                return True
        return False


    def addCardAndSolve(self,newCard):
        if(self.Duplicates(newCard)):
            # Checks for sets with the new card and the cardlist then adds the card to the list
            print("Duplicate card")

            dlg = CustomDialog()
            if not (dlg.exec()):
                print("Duplicate canceled")
                return False

        for i,firstCard in enumerate(self.cardList):
            for secondCard in self.cardList[i+1:]:
                if self.isSet(firstCard,secondCard,newCard):
                    self.foundSets.append([newCard.location,firstCard.location,secondCard.location])

        self.cardList.append(newCard)
        return True
            
        
        

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
            for s in self.foundSets:
                if location in s:
                    self.foundSets.remove(s)
    
    def clearAll(self):
        # Clears the cardlist and the found sets
        self.cardList.clear()
        self.foundSets.clear()

        

class MyWindow(QWidget) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.setWindowIcon(QIcon("SetCards/RFW3.png"))
        self.initUI()

    def initUI(self):

        def newRadioButton(name, gridAttribute, horizontalAttribute) :
            radioButtonName = ("radioButton" + name)
            radioButton = QtWidgets.QRadioButton(gridAttribute)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)
            radioButton.setObjectName(radioButtonName)
            radioButton.setText(name)
            radioButton.clicked.connect(self.UpdateCard)

            setattr(self, radioButtonName, radioButton)

            horizontalAttribute.addWidget(radioButton)


        grid_layout = QGridLayout()

        # Set the layout for the main window
        self.setLayout(grid_layout)



        self.gridLayoutWidgetShape = QtWidgets.QWidget(self)
        self.gridLayoutWidgetShape.setGeometry(QtCore.QRect(450, 10, 700, 231))
        self.gridLayoutCardOptions = QtWidgets.QGridLayout(self.gridLayoutWidgetShape)
        self.gridLayoutCardOptions.setObjectName("gridLayoutCardOptions")
        self.gridLayoutWidgetShape.setObjectName("gridLayoutWidgetShape")
        self.frame_4 = QtWidgets.QFrame(self.gridLayoutWidgetShape)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.horizontalLayoutWidgetCardOptions = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidgetCardOptions.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.horizontalLayoutWidgetCardOptions.setObjectName("horizontalLayoutWidgetCardOptions")
        self.horizontalLayoutCardOptions = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetCardOptions)
        self.horizontalLayoutCardOptions.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayoutCardOptions.setObjectName("horizontalLayoutCardOptions")
        self.labelShape = QtWidgets.QLabel(self.horizontalLayoutWidgetCardOptions)
        self.labelShape.setObjectName("labelShape")
        self.labelShape.setText("Shape:")
        self.horizontalLayoutCardOptions.addWidget(self.labelShape)


        newRadioButton("Wave", self.gridLayoutWidgetShape, self.horizontalLayoutCardOptions)
        newRadioButton("Oval", self.gridLayoutWidgetShape, self.horizontalLayoutCardOptions)
        newRadioButton("Diamond", self.gridLayoutWidgetShape, self.horizontalLayoutCardOptions)

        self.gridLayoutCardOptions.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frameCardOptions = QtWidgets.QFrame(self.gridLayoutWidgetShape)
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

        newRadioButton("Red", self.horizontalLayoutWidgetColor, self.horizontalLayoutColor)
        newRadioButton("Green", self.horizontalLayoutWidgetColor, self.horizontalLayoutColor)
        newRadioButton("Purple", self.horizontalLayoutWidgetColor, self.horizontalLayoutColor)

        self.gridLayoutCardOptions.addWidget(self.frameCardOptions, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.gridLayoutWidgetShape)
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

        newRadioButton("1", self.horizontalLayoutWidget_Color, self.horizontalLayout_4)
        newRadioButton("2", self.horizontalLayoutWidget_Color, self.horizontalLayout_4)
        newRadioButton("3", self.horizontalLayoutWidget_Color, self.horizontalLayout_4)

        self.gridLayoutCardOptions.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.gridLayoutWidgetShape)
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

        newRadioButton("Full", self.horizontalLayoutWidget_5, self.horizontalLayout_5)
        newRadioButton("Half", self.horizontalLayoutWidget_5, self.horizontalLayout_5)
        newRadioButton("Empty", self.horizontalLayoutWidget_5, self.horizontalLayout_5)

        self.gridLayoutCardOptions.addWidget(self.frame_7, 3, 0, 1, 1)
        self.NewCard = QtWidgets.QLabel(self.gridLayoutWidgetShape)
        self.NewCard.setObjectName("NewCard")
        self.NewCard.setText("Image of user generated card")
        self.gridLayoutCardOptions.addWidget(self.NewCard, 0, 1, 3, 1)

        self.AddCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.AddCardButton.setObjectName("AddCardButton")
        self.AddCardButton.setText("Add Card")
        self.gridLayoutCardOptions.addWidget(self.AddCardButton, 1, 1, 3, 1)
        self.AddCardButton.clicked.connect(self.ChangeCard)  # Connect the clicked signal of the AddCardButton to the ChangeCard method

        self.DeleteCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.DeleteCardButton.setObjectName("DeleteCardButton")
        self.DeleteCardButton.setText("Delete Card")
        self.gridLayoutCardOptions.addWidget(self.DeleteCardButton, 2, 1, 3, 1)
        self.DeleteCardButton.clicked.connect(self.DeleteCard)

        self.WipeDeckButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.WipeDeckButton.setObjectName("WipeDeckButton")
        self.WipeDeckButton.setText("Wipe Deck")
        self.gridLayoutCardOptions.addWidget(self.WipeDeckButton, 3, 1, 3, 1)
        self.WipeDeckButton.clicked.connect(self.wipeDeck)



        grid_layout.addWidget(self.gridLayoutWidgetShape, 0, 15, 3, 4)  # Add the card options widget to the main layout and set its position to 2x2

        self.setLayout(grid_layout)  # Set the layout for the main window
        self.grid_layout = grid_layout
        # Create the grid layout


        self.solver = SetSolver()
        self.reset()


    def reset(self):
        for i in range(4):
            for j in range(3):
                # creates card based on i and j and random values and solves them and shows them
                while(True):
                    location = Location(i,j)
                    card = Card("E", "E", "E", "0", location)
                    self.showCard(card, self.grid_layout)
                    break


                    # card = Card(random.choice(["Purple","Green","Red"]),random.choice(["D","W","O"]),random.choice(["E","F","L"]),random.choice(["1","2","3"]),location)
                    # if (self.solver.noDuplicates(card)):
                    #     self.solver.addCardAndSolve(card)
                    #     self.showCard(card,self.grid_layout)
                    #     break
        #Todo change name from set to something better because name set is python name

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

        if self.radioButton1.isChecked():
            amount = "1"
        elif self.radioButton2.isChecked():
            amount = "2"
        elif self.radioButton3.isChecked():
            amount = "3"

        image = QImage(f"SetCards/R{filling}{shape}{amount}.png")
        image = image.convertToFormat(QImage.Format.Format_RGB32)
        for i in range(image.width()):
            for j in range(image.height()):
                if image.pixelColor(i,j).black()==0:
                    image.setPixelColor(i,j,QColor(color))
        pixmap = QPixmap.fromImage(image)

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

        if self.radioButton1.isChecked():
            amount = "1"
        elif self.radioButton2.isChecked():
            amount = "2"
        elif self.radioButton3.isChecked():
            amount = "3"

        card = Card(color, shape, filling, amount, self.selectedLocation)
        solver = SetSolver()
        solver.removeCard(self.selectedLocation)

        if solver.addCardAndSolve(card):
            self.showCard(card, self.grid_layout)

        for set in self.solver.foundSets:
            print(f"{set[0]} and {set[1]} and {set[2]}")
            MyWindow.showSets(self)

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
        # Removes the clicked button from the grid
        button = self.sender()
        position = self.grid_layout.getItemPosition(self.grid_layout.indexOf(button))
        pixel_position = button.pos()
        print(pixel_position)

        x = position[0]
        y = position[1]
        self.selectedLocation = Location(x,y)
        card = self.solver.getCard(Location(x,y))
        if card is not None:

            self.DeleteCardButton.show()

            if card.color == "Red":
                self.radioButtonRed.setChecked(True)
            elif card.color == "Green":
                self.radioButtonGreen.setChecked(True)
            elif card.color == "Purple":
                self.radioButtonPurple.setChecked(True)

            if card.shape == "W":
                self.radioButtonWave.setChecked(True)
            elif card.shape == "O":
                self.radioButtonOval.setChecked(True)
            elif card.shape == "D":
                self.radioButtonDiamond.setChecked(True)
            
            if card.filling == "F":
                self.radioButtonFull.setChecked(True)
            elif card.filling == "L":
                self.radioButtonHalf.setChecked(True)
            elif card.filling == "E":
                self.radioButtonEmpty.setChecked(True)
            
            if card.amount == "1":
                self.radioButton1.setChecked(True)
            elif card.amount == "2":
                self.radioButton2.setChecked(True)
            elif card.amount == "3":
                self.radioButton3.setChecked(True)


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

              # Connect the clicked signal of the DeleteCardButton to the DeleteCard method

        else:
            print(f"Card not found at location {x},{y}")
            self.DeleteCardButton.hide()  # Hide the DeleteCardButton if card is None\

            self.radioButtonRed.setChecked(True)
            self.radioButtonGreen.setChecked(False)
            self.radioButtonPurple.setChecked(False)
            
            self.radioButtonWave.setChecked(True)
            self.radioButtonOval.setChecked(False)
            self.radioButtonDiamond.setChecked(False)
        
            self.radioButtonFull.setChecked(True)
            self.radioButtonHalf.setChecked(False)
            self.radioButtonEmpty.setChecked(False)
        
            self.radioButton1.setChecked(True)
            self.radioButton2.setChecked(False)
            self.radioButton3.setChecked(False)
            

        self.update()


    def DeleteCard(self):
        # Removes the clicked card from the UI and the solver
        selectedLocation = self.selectedLocation
        print(selectedLocation)
        self.solver.removeCard(selectedLocation)
        self.addImage(self.grid_layout, "SetCards/REE0.png", selectedLocation.x, selectedLocation.y, QColor("white"))

        print(f"Deleted card at location {selectedLocation}")
    
    def wipeDeck(self):
        # Clears the deck
        self.solver.clearAll()
        for i in range(4):
            for j in range(3):
                self.addImage(self.grid_layout, "SetCards/REE0.png", i, j, QColor("white"))
        self.update()

    def showSets(self):


        for set in self.solver.foundSets:
            card1 = set[0]
            card2 = set[1]
            card3 = set[2]

        pixel_position = self.pos()
        print(pixel_position)
        self.drawLines()

        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red))
        painter.drawLine(10, 10, 300, 300)
        painter.end()

        # center1 = QPoint(card1.location.x, card1.location.y)
        print(card1)
        print(card2)
        print(card3)
  

    # def paintEvent(self, event):
    #     self.drawLines()


    # def drawLines(self):
    #     painter = QPainter(self)
    #     painter.setPen(QPen(Qt.GlobalColor.red))
    #     painter.drawLine(10, 10, 300, 300)
    #     # pixel_position = self.pos()
    #     # painter.drawLine(pixel_position.x, pixel_position.y, 400, 400)


    #     # painter.drawLine(center1, center2)
    #     # painter.drawLine(center2, center3)
    #     # painter.drawLine(center3, center1)

    #     painter.end()


    def update(self):
        self.label.adjustSize()



def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


window()
