import sys

from PyQt5 import QtWidgets

import Plantilla_Juego as grafica
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas


class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action)

        self.btn_arriba.clicked.connect(self.mover)
        self.btn_izquierda.clicked.connect(self.mover)
        self.btn_centro.clicked.connect(self.mover)
        self.btn_derecha.clicked.connect(self.mover)
        self.btn_abajo.clicked.connect(self.mover)

        ################################################################################

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5


        #################################################################################
        #                Jugador  Computadora
        self.personajes = [[0, 0], [0, 0]]

        ##############################################

        self.limpiar()



    # Área de los Slots
    def mover(self):
        nombre_btn= self.sender().objectName()
        accion = nombre_btn.split("_")[1]
        print(nombre_btn," accion:", accion)

        Xusuario = self.personajes[0][0]
        Yusuario = self.personajes[0][1]

        if accion == "arriba": #v  => valor de x
            if Yusuario + 1 <= self.yMax:
                self.personajes[0][1] = Yusuario + 1
            else:
                self.personajes[0][1] = self.yMin

        elif accion == "abajo":
            if Yusuario - 1 >= self.yMin:
                self.personajes[0][1] = Yusuario - 1
            else:
                self.personajes[0][1] = self.yMax

        elif accion == "izquierda": # v  => valor de x
            if Xusuario - 1 >= self.xMin:
                self.personajes[0][0] = Xusuario - 1
            else:
                self.personajes[0][0] = self.xMax

        elif accion == "derecha": # v  => valor de x
            if Xusuario + 1 <= self.xMax:
                self.personajes[0][0] = Xusuario + 1
            else:
                self.personajes[0][0] = self.xMin


        else:
            self.personajes[0][0] = 0
            self.personajes[0][1] = 0

        self.limpiar()
        self.graficar()
    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.btn_action.setText("DETENER")

            #jugador
            self.personajes[0] = [0, 0] #vuelve al jugar al centro

            import random as rnd
            #computadora
            self.personajes[1] = [rnd.randrange(self.xMin, self.xMax),
                                  rnd.randrange(self.yMin, self.yMax)]
            self.graficar()
        else:
            self.btn_action.setText("INICIAR")
            self.limpiar()


    def limpiar(self):
        plt.cla() #BORRA_TODO EL GRAFICO

        x = [i for i in range(self.xMin, self.xMax + 1)] #GENERA LOS TICKS
        y = [i for i in range(self.yMin, self.yMax + 1)] #GENERA LOS TICKS

        self.ax.set_xticks(x)
        self.ax.set_yticks(y)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)  #CUADRICULA

        self.canvas.draw() #DIBUJAR EL GRAFICO


    def graficar(self):

        #POSICIONA AL USUARIO EN LA GRAFICA
        self.ax.plot(self.personajes[0][0], self.personajes[0][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="yellow",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        #POSICIONA A LA COMPUTADORA EN EL GRAFICO
        self.ax.plot(self.personajes[1][0], self.personajes[1][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="green",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        self.canvas.draw() #DIBUJA EL GRAFICO

        #COMPRUEBA CADA QUE SE GRAFICA SI EL USUARIO ALCANZO A LA COMPUTADORA
        #SI LAS COORDENADAS DE AMBOS ESTAN EN LA MISMA POSICION, ENTONCES EL USUARIO ALCANZO
        # A LA COMPUTADORA..
        if self.personajes[0][0] == self.personajes[1][0] and self.personajes[0][1] == self.personajes[1][1]:
            self.limpiar()
            m = QtWidgets.QMessageBox()
            m.setText("Has Ganado")
            m.exec_()
            self.btn_action.setText("INICIAR")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())