from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 422)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        MainWindow.setFont(font)
        MainWindow.setWindowFilePath("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        def newGridBox(i, x, y) :
            self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
            self.graphicsView.setObjectName("graphicsView" + str(i))
            self.graphicsView.setAutoFillBackground(True)
            self.gridLayout.addWidget(self.graphicsView, y, x, 1, 1)

        # Create gridBoxes
        i = 0
        for y in range (0,4) :
            if y > 0 :
                y = y + 1

            for x in range(0,3) :
                newGridBox(i, x, y)
                i = i + 1

#### RIGHT SIDE BEGINS HERE.

        self.gridLayoutWidgetCardOptions = QtWidgets.QWidget(self.centralwidget)
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
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonWave)

        self.radioButtonOval = QtWidgets.QRadioButton(self.horizontalLayoutWidgetCardOptions)
        self.radioButtonOval.setAutoExclusive(True)
        self.radioButtonOval.setObjectName("radioButtonOval")
        self.radioButtonOval.setText("Oval")
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonOval)

        self.radioButtonDiamond = QtWidgets.QRadioButton(self.horizontalLayoutWidgetCardOptions)
        self.radioButtonDiamond.setAutoExclusive(True)
        self.radioButtonDiamond.setObjectName("radioButtonDiamond")
        self.radioButtonDiamond.setText("Diamond")
        self.horizontalLayoutCardOptions.addWidget(self.radioButtonDiamond)

        self.gridLayoutCardOptions.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frameCardOptions = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frameCardOptions.setFont(font)
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
        self.horizontalLayoutColor.addWidget(self.radioButtonRed)

        self.radioButtonGreen = QtWidgets.QRadioButton(self.horizontalLayoutWidgetColor)
        self.radioButtonGreen.setAutoExclusive(True)
        self.radioButtonGreen.setObjectName("radioButtonGreen")
        self.radioButtonGreen.setText("Green")
        self.horizontalLayoutColor.addWidget(self.radioButtonGreen)

        self.radioButtonPurple = QtWidgets.QRadioButton(self.horizontalLayoutWidgetColor)
        self.radioButtonPurple.setAutoExclusive(True)
        self.radioButtonPurple.setObjectName("radioButtonPurple")
        self.radioButtonPurple.setText("Purple")
        self.horizontalLayoutColor.addWidget(self.radioButtonPurple)


        self.gridLayoutCardOptions.addWidget(self.frameCardOptions, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frame_6.setFont(font)
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
        self.horizontalLayout_4.addWidget(self.radioButtonColor1)

        self.radioButtonColor2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_Color)
        self.radioButtonColor2.setAutoExclusive(True)
        self.radioButtonColor2.setObjectName("radioButtonColor2")
        self.radioButtonColor2.setText("2")
        self.horizontalLayout_4.addWidget(self.radioButtonColor2)

        self.radioButtonColor3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_Color)
        self.radioButtonColor3.setAutoExclusive(True)
        self.radioButtonColor3.setObjectName("radioButtonColor3")
        self.radioButtonColor3.setText("3")
        self.horizontalLayout_4.addWidget(self.radioButtonColor3)


        self.gridLayoutCardOptions.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.gridLayoutWidgetCardOptions)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frame_7.setFont(font)
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
        self.horizontalLayout_5.addWidget(self.radioButtonFull)

        self.radioButtonHalf = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButtonHalf.setAutoExclusive(True)
        self.radioButtonHalf.setObjectName("radioButtonHalf")
        self.radioButtonHalf.setText("Half")
        self.horizontalLayout_5.addWidget(self.radioButtonHalf)

        self.radioButtonEmpty = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButtonEmpty.setAutoExclusive(True)
        self.radioButtonEmpty.setObjectName("radioButtonEmpty")
        self.radioButtonEmpty.setText("Empty")
        self.horizontalLayout_5.addWidget(self.radioButtonEmpty)

        self.gridLayoutCardOptions.addWidget(self.frame_7, 3, 0, 1, 1)
        self.NewCard = QtWidgets.QLabel(self.gridLayoutWidgetCardOptions)
        self.NewCard.setObjectName("NewCard")
        self.NewCard.setText("Image of user generated card")
        self.gridLayoutCardOptions.addWidget(self.NewCard, 0, 1, 3, 1)
        self.AddCardButton = QtWidgets.QPushButton(self.gridLayoutWidgetCardOptions)
        self.AddCardButton.setObjectName("AddCardButton")
        self.AddCardButton.setText("Add Card")

        self.gridLayoutCardOptions.addWidget(self.AddCardButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
