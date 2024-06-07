from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class SetSolver():
    cardList = []
    foundSetLocations = []
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

            dlg = DuplicateDialog()
            if not (dlg.exec()):
                print("Duplicate canceled")
                return False

        for i,firstCard in enumerate(self.cardList):
            for secondCard in self.cardList[i+1:]:
                if self.isSet(firstCard,secondCard,newCard):
                    self.foundSetLocations.append([newCard.location,firstCard.location,secondCard.location])
                    self.foundSets.append([newCard,firstCard,secondCard])
                    

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
            for s in self.foundSetLocations:
                if location in s:
                    self.foundSetLocations.remove(s)
            
           
            for s in self.foundSets:
                if card in s:
                    self.foundSets.remove(s)
    
    def clearAll(self):
        # Clears the cardlist and the found sets
        self.cardList.clear()
        self.foundSetLocations.clear()

