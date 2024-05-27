from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt,QPoint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
import random

import sys

WINHEIGHT = 400
WINWIDTH = 800
class Location():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"

class Card():
    def __init__(self,color,shape,filling,amount,location):
        self.color = color
        self.shape = shape
        self.filling = filling
        self.amount = amount
        self.location = location
class SetSolver():
    cardList = []
    foundSets = []
    def __init__(self):
        pass
    def addCardAndSolve(self,newCard):
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


class MyWindow(QWidget) :    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(50, 200, WINWIDTH, WINHEIGHT)
        self.setWindowTitle("Set Solver")
        self.setWindowIcon(QIcon("SetCards/RFW3.png"))
        self.initUI()

    def paintEvent(self, event):
        # Ensure QPainter is only used within paintEvent
        painter = QPainter(self)
        # Check if the QPainter is active
        if painter.isActive():
            # Create a QPen object to define the line style
            pen = QPen()
            pen.setWidth(5)  # Set the line width
            pen.setColor(Qt.GlobalColor.blue)  # Set the line color
            painter.setPen(pen)
            
            # Draw a line from point (50, 50) to point (200, 200)
            painter.drawLine(self.line_start[0], self.line_start[1], self.line_end[0], self.line_end[1])
            
            # You can draw more lines or shapes here if needed
        
        # End the QPainter explicitly (optional, as it will be done automatically when painter is deleted)
        painter.end()

    def draw_line(self,x1,y1,x2,y2):
        # Store the coordinates of the line
        self.line_start = (x1, y1)
        self.line_end = (x2, y2)
        
        # Trigger a repaint
        self.update()

 
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        # makes a 3 by 4 grid with random cards
        solver = SetSolver()
        for i in range(3):
            for j in range(4):
                # creates card based on i and j and random values and solves them and shows them
                location = Location(i,j)
                card = Card(random.choice(["purple","green","red"]),random.choice(["D","W","O"]),random.choice(["E","F","L"]),random.choice(["1","2","3"]),location)
                solver.addCardAndSolve(card)
                self.showCard(card,grid)
        #Todo change name from set to something better because name set is python name
        for set in solver.foundSets:
            print(f"{set[0]} and {set[1]} and {set[2]}")
            self.draw_line(int(set[0].x*self.size().width()/4)
                           ,int(set[0].y*self.size().height()/4)
                           ,int(set[1].x*self.size().width()/4)
                           ,int(set[1].y*self.size().height()/4))
        
    def showCard(self,card,grid):
        # Adds the card to the UI based on a card object
        self.addImage(grid,f"SetCards/R{card.filling}{card.shape}{card.amount}.png",card.location.x,card.location.y,QColor(card.color))
    def addImage(self, grid, filelocation,x,y,color):
        # Creates and shows an image on the grid at x,y of file at filelocation with color color
        image = QImage(filelocation)
        image = image.convertToFormat(QImage.Format.Format_RGB32)
        for i in range(image.width()):
            for j in range(image.height()):
                if image.pixelColor(i,j).black()==0:
                    image.setPixelColor(i,j,color)
        pixmap = QPixmap.fromImage(image)
        label = QLabel(self)
        label.setPixmap(pixmap)
        grid.addWidget(label, x, y)
    
    def button1Clicked(self):
        # Unused function?
        self.label.setText("hellllll wat")
        self.update()
    
    # def update(self):
    #     self.label.adjustSize()


    

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


window()