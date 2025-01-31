from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.py as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as  FiguraCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as BarraNavegacion


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 130, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 200, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 250, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 290, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 340, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 380, 91, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 10, 151, 41))
        self.label_7.setObjectName("label_7")
        self.combo_coloreslinea = QtWidgets.QComboBox(self.centralwidget)
        self.combo_coloreslinea.setGeometry(QtCore.QRect(520, 60, 161, 21))
        self.combo_coloreslinea.setObjectName("combo_coloreslinea")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 80, 101, 31))
        self.label_8.setObjectName("label_8")
        self.combo_estilolinea = QtWidgets.QComboBox(self.centralwidget)
        self.combo_estilolinea.setGeometry(QtCore.QRect(330, 110, 111, 31))
        self.combo_estilolinea.setObjectName("combo_estilolinea")
        self.btn_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpiar.setGeometry(QtCore.QRect(330, 30, 111, 31))
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.spin_xmin = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_xmin.setGeometry(QtCore.QRect(550, 130, 121, 31))
        self.spin_xmin.setObjectName("spin_xmin")
        self.spin_xmax = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_xmax.setGeometry(QtCore.QRect(560, 190, 121, 31))
        self.spin_xmax.setObjectName("spin_xmax")
        self.spin_xdivisiones = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_xdivisiones.setGeometry(QtCore.QRect(560, 250, 121, 31))
        self.spin_xdivisiones.setObjectName("spin_xdivisiones")
        self.spin_ymin = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_ymin.setGeometry(QtCore.QRect(560, 290, 121, 31))
        self.spin_ymin.setObjectName("spin_ymin")
        self.spin_ydiviones = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_ydiviones.setGeometry(QtCore.QRect(560, 330, 121, 31))
        self.spin_ydiviones.setObjectName("spin_ydiviones")
        self.spin_ancholinea = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_ancholinea.setGeometry(QtCore.QRect(540, 410, 121, 31))
        self.spin_ancholinea.setObjectName("spin_ancholinea")
        self.btn_grilla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_grilla.setGeometry(QtCore.QRect(100, 190, 91, 31))
        self.btn_grilla.setObjectName("btn_grilla")
        self.btn_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graficar.setGeometry(QtCore.QRect(190, 40, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_graficar.setFont(font)
        self.btn_graficar.setObjectName("btn_graficar")
        self.btn_establecer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_establecer.setGeometry(QtCore.QRect(190, 120, 91, 31))
        self.btn_establecer.setObjectName("btn_establecer")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 100, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 70, 131, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(310, 40, 20, 181))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 280, 321, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_polinomio = QtWidgets.QLineEdit(self.centralwidget)
        self.line_polinomio.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.line_polinomio.setObjectName("line_polinomio")
        self.line_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_titulo.setGeometry(QtCore.QRect(70, 130, 113, 20))
        self.line_titulo.setObjectName("line_titulo")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 200, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.figure = plt.figure(figsize=(15,5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.addsubplot(111)

        self.toolbar = BarraNavegacion(self.canvas, self)

        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.toolbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Xmin:"))
        self.label_2.setText(_translate("MainWindow", "Xmax:"))
        self.label_3.setText(_translate("MainWindow", "T.Divisiones:"))
        self.label_4.setText(_translate("MainWindow", "Ymin:"))
        self.label_5.setText(_translate("MainWindow", "T.Divisiones"))
        self.label_6.setText(_translate("MainWindow", "Ancho de la Línea"))
        self.label_7.setText(_translate("MainWindow", "Colores de la Línea:"))
        self.label_8.setText(_translate("MainWindow", "Estilo de la Línea"))
        self.btn_limpiar.setText(_translate("MainWindow", "LIMPIAR GRÁFICO"))
        self.label_9.setText(_translate("MainWindow", "Polinomio:"))
        self.label_10.setText(_translate("MainWindow", "Título:"))
        self.btn_grilla.setText(_translate("MainWindow", "OFF"))
        self.btn_graficar.setText(_translate("MainWindow", "Graficar"))
        self.btn_establecer.setText(_translate("MainWindow", "Establecer"))
        self.label_11.setText(_translate("MainWindow", "Grilla"))
