# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Juego_Completo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas
import recursos_programas_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 538)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 501, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_action = QtWidgets.QPushButton(self.centralwidget)
        self.btn_action.setGeometry(QtCore.QRect(560, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_action.setFont(font)
        self.btn_action.setStyleSheet("font: 20pt \"MS Serif\";\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_action.setObjectName("btn_action")
        self.lbTiempo = QtWidgets.QLabel(self.centralwidget)
        self.lbTiempo.setGeometry(QtCore.QRect(560, 100, 241, 41))
        self.lbTiempo.setStyleSheet("font: 20pt \"MS Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lbTiempo.setObjectName("lbTiempo")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(560, 220, 251, 251))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_arriba = QtWidgets.QPushButton(self.groupBox)
        self.btn_arriba.setGeometry(QtCore.QRect(90, 10, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_arriba.setFont(font)
        self.btn_arriba.setStyleSheet("border-image: url(:/Juego/Uarrow.png);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_arriba.setText("")
        self.btn_arriba.setObjectName("btn_arriba")
        self.btn_derecha = QtWidgets.QPushButton(self.groupBox)
        self.btn_derecha.setGeometry(QtCore.QRect(170, 90, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_derecha.setFont(font)
        self.btn_derecha.setStyleSheet("border-image: url(:/Juego/Rarrow.png);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_derecha.setText("")
        self.btn_derecha.setObjectName("btn_derecha")
        self.btn_izquierda = QtWidgets.QPushButton(self.groupBox)
        self.btn_izquierda.setGeometry(QtCore.QRect(10, 90, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_izquierda.setFont(font)
        self.btn_izquierda.setStyleSheet("border-image: url(:/Juego/Larrow.png);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_izquierda.setText("")
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.btn_centro = QtWidgets.QPushButton(self.groupBox)
        self.btn_centro.setGeometry(QtCore.QRect(90, 90, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_centro.setFont(font)
        self.btn_centro.setStyleSheet("border-image: url(:/Juego/centro.png);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_centro.setText("")
        self.btn_centro.setObjectName("btn_centro")
        self.btn_abajo = QtWidgets.QPushButton(self.groupBox)
        self.btn_abajo.setGeometry(QtCore.QRect(90, 170, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abajo.setFont(font)
        self.btn_abajo.setStyleSheet("border-image: url(:/Juego/Darrow.png);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_abajo.setText("")
        self.btn_abajo.setObjectName("btn_abajo")
        self.lbEnemigos = QtWidgets.QLabel(self.centralwidget)
        self.lbEnemigos.setGeometry(QtCore.QRect(560, 160, 241, 41))
        self.lbEnemigos.setStyleSheet("font: 20pt \"MS Serif\";\n"
"color: rgb(255, 255, 255);")
        self.lbEnemigos.setObjectName("lbEnemigos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.verticalLayout.addWidget(self.canvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_action.setText(_translate("MainWindow", "INICIAR"))
        self.lbTiempo.setText(_translate("MainWindow", "Tiempo:"))
        self.lbEnemigos.setText(_translate("MainWindow", "Enemigos:"))