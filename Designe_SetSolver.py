# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_SetSolver.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 422)
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
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 4, 0, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 2, 0, 1, 1)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout.addWidget(self.graphicsView_7, 2, 1, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 3, 0, 1, 1)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.gridLayout.addWidget(self.graphicsView_5, 4, 1, 1, 1)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout.addWidget(self.graphicsView_6, 3, 1, 1, 1)
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.gridLayout.addWidget(self.graphicsView_10, 2, 2, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout.addWidget(self.graphicsView_9, 0, 2, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout.addWidget(self.graphicsView_8, 0, 1, 1, 1)
        self.graphicsView_12 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.gridLayout.addWidget(self.graphicsView_12, 4, 2, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_11 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_11.setObjectName("graphicsView_11")
        self.gridLayout.addWidget(self.graphicsView_11, 3, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(450, 10, 341, 231))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frame_5.setFont(font)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 163, 26))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)

        self.radioButton_Wave = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_Wave.setChecked(True)
        self.radioButton_Wave.setAutoExclusive(True)
        self.radioButton_Wave.setObjectName("radioButton_Wave")
        self.radioButton_Wave.setText("Wave")
        self.horizontalLayout_3.addWidget(self.radioButton_Wave)

        self.radioButton_Oval = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_Oval.setChecked(False)
        self.radioButton_Oval.setAutoExclusive(True)
        self.radioButton_Oval.setObjectName("radioButton_Oval")
        self.radioButton_Oval.setText("Oval")
        self.horizontalLayout_3.addWidget(self.radioButton_Oval)

        self.radioButton_22 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_22.setChecked(False)
        self.radioButton_22.setAutoExclusive(True)
        self.radioButton_22.setObjectName("radioButton_22")
        self.horizontalLayout_3.addWidget(self.radioButton_22)
        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frame_3.setFont(font)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 40, 35, 10))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 160, 26))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.radioButton_18 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_18.setChecked(True)
        self.radioButton_18.setAutoExclusive(True)
        self.radioButton_18.setObjectName("radioButton_18")
        self.horizontalLayout_2.addWidget(self.radioButton_18)
        self.radioButton_17 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_17.setChecked(False)
        self.radioButton_17.setAutoExclusive(True)
        self.radioButton_17.setObjectName("radioButton_17")
        self.horizontalLayout_2.addWidget(self.radioButton_17)
        self.radioButton_19 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_19.setChecked(False)
        self.radioButton_19.setAutoExclusive(True)
        self.radioButton_19.setObjectName("radioButton_19")
        self.horizontalLayout_2.addWidget(self.radioButton_19)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        self.frame_6.setFont(font)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_6)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 161, 26))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.radioButton_23 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_23.setChecked(True)
        self.radioButton_23.setAutoExclusive(True)
        self.radioButton_23.setObjectName("radioButton_23")
        self.horizontalLayout_4.addWidget(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_24.setChecked(False)
        self.radioButton_24.setAutoExclusive(True)
        self.radioButton_24.setObjectName("radioButton_24")
        self.horizontalLayout_4.addWidget(self.radioButton_24)
        self.radioButton_25 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_25.setChecked(False)
        self.radioButton_25.setAutoExclusive(True)
        self.radioButton_25.setObjectName("radioButton_25")
        self.horizontalLayout_4.addWidget(self.radioButton_25)
        self.gridLayout_4.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(8)
        self.frame_7.setFont(font)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 179, 26))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.radioButton_28 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_28.setChecked(True)
        self.radioButton_28.setAutoExclusive(True)
        self.radioButton_28.setObjectName("radioButton_28")
        self.horizontalLayout_5.addWidget(self.radioButton_28)
        self.radioButton_27 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_27.setChecked(False)
        self.radioButton_27.setAutoExclusive(True)
        self.radioButton_27.setObjectName("radioButton_27")
        self.horizontalLayout_5.addWidget(self.radioButton_27)
        self.radioButton_26 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_26.setChecked(False)
        self.radioButton_26.setAutoExclusive(True)
        self.radioButton_26.setObjectName("radioButton_26")
        self.horizontalLayout_5.addWidget(self.radioButton_26)
        self.gridLayout_4.addWidget(self.frame_7, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 3, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     self.label_8.setText(_translate("MainWindow", "Shape:"))
    #     self.radioButton_20.setText(_translate("MainWindow", "Oval"))
    #     self.radioButton_22.setText(_translate("MainWindow", "Diamond"))
    #     self.label_7.setText(_translate("MainWindow", "Color:"))
    #     self.radioButton_18.setText(_translate("MainWindow", "Red"))
    #     self.radioButton_17.setText(_translate("MainWindow", "Green"))
    #     self.radioButton_19.setText(_translate("MainWindow", "Purple"))
    #     self.label_9.setText(_translate("MainWindow", "Amount:"))
    #     self.radioButton_23.setText(_translate("MainWindow", "1"))
    #     self.radioButton_24.setText(_translate("MainWindow", "2"))
    #     self.radioButton_25.setText(_translate("MainWindow", "3"))
    #     self.label_2.setText(_translate("MainWindow", "Filling:"))
    #     self.radioButton_28.setText(_translate("MainWindow", "Full"))
    #     self.radioButton_27.setText(_translate("MainWindow", "Half"))
    #     self.radioButton_26.setText(_translate("MainWindow", "Empty"))
    #     self.label_3.setText(_translate("MainWindow", "Image of user generated card"))
    #     self.pushButton.setText(_translate("MainWindow", "Add Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())