from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from SetSolver import *
from Location import *
from Card import *


WINWIDTH = 1500
WINHEIGHT = 400

class MyWindow(QWidget) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.setWindowIcon(QIcon("SetCards/RFW3.png"))
        self.initUI()
        self.selectedLocation = Location(0,0)
        self.radioButtonRed.setChecked(True)
        self.radioButtonWave.setChecked(True)
        self.radioButtonFull.setChecked(True)
        self.radioButton1.setChecked(True)

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
        self.gridLayoutWidgetShape.setMinimumWidth(1100)
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
        self.gridLayoutCardOptions.addWidget(self.NewCard, 0, 2, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.AddCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.AddCardButton.setObjectName("AddCardButton")
        self.AddCardButton.setText("Add Card")
        self.gridLayoutCardOptions.addWidget(self.AddCardButton, 1, 2, 3, 1)
        self.AddCardButton.clicked.connect(self.ChangeCard)  # Connect the clicked signal of the AddCardButton to the ChangeCard method

        self.DeleteCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.DeleteCardButton.setObjectName("DeleteCardButton")
        self.DeleteCardButton.setText("Delete Card")
        self.gridLayoutCardOptions.addWidget(self.DeleteCardButton, 2, 2, 3, 1)
        self.DeleteCardButton.clicked.connect(self.DeleteCard)

        self.WipeDeckButton = QtWidgets.QPushButton(self.gridLayoutWidgetShape)
        self.WipeDeckButton.setObjectName("WipeDeckButton")
        self.WipeDeckButton.setText("Wipe Deck")
        self.gridLayoutCardOptions.addWidget(self.WipeDeckButton, 3, 2, 3, 1)
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

    def showSetCards(self, card, grid_layout, locationX, locationY):
        self.addImage(grid_layout, f"SetCards/R{card.filling}{card.shape}{card.amount}.png", locationX, locationY, QColor(card.color))



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

        for set in self.solver.foundSetLocations:
            print(f"{set[0]} and {set[1]} and {set[2]}")
            MyWindow.showSets(self)
        self.firstEmptyCardSlot()

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


            self.NewCard.setPixmap(pixmap)

        else:
            print(f"Card not found at location {x},{y}")
            self.DeleteCardButton.hide()  # Hide the DeleteCardButton if card is None

        self.update()


    def DeleteCard(self):
        # Removes the clicked card from the UI and the solver
        selectedLocation = self.selectedLocation
        print(selectedLocation)
        self.solver.removeCard(selectedLocation)
        self.showSets()
        self.addImage(self.grid_layout, "SetCards/REE0.png", selectedLocation.x, selectedLocation.y, QColor("white"))

        print(f"Deleted card at location {selectedLocation}")
    
    def wipeDeck(self):
        # Clears the deck
        self.solver.clearAll()
        for i in range(4):
            for j in range(3):
                self.addImage(self.grid_layout, "SetCards/REE0.png", i, j, QColor("white"))
        self.solver.foundSets.clear()
        self.showSets()
        self.update()

    def showSets(self):

        print(self.solver.foundSets)
        totalNumberOfSets = len(self.solver.foundSets)
        print(totalNumberOfSets)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollContent = QWidget()
        scrollLayout = QGridLayout(scrollContent)

        for i in range(totalNumberOfSets):
            for j in range(3):
                card = self.solver.foundSets[i][j]
                self.showSetCards(card, scrollLayout, i, j)

        scrollArea.setWidget(scrollContent)
        self.gridLayoutCardOptions.addWidget(scrollArea, 6, 2, 1, 1)


    def update(self):
        self.label.adjustSize()
    
    def firstEmptyCardSlot(self):
        for x in range(4):
            for y in range(3):
                # print(self.solver.getCard(Location(x,y)))
                # print(Location(x,y))
                print(self.selectedLocation)
                if(self.solver.getCard(Location(x,y)) is None):
                    self.selectedLocation = Location(x,y)
                    return