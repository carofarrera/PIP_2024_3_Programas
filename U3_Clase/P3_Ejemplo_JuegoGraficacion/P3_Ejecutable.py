import random
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import Qt

import Juego_Completo as grafica
import matplotlib.pyplot as plt
import random as rnd


class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action) # Iniciar

        self.btn_arriba.clicked.connect(self.mover)
        self.btn_izquierda.clicked.connect(self.mover)
        self.btn_centro.clicked.connect(self.mover)
        self.btn_derecha.clicked.connect(self.mover)
        self.btn_abajo.clicked.connect(self.mover)

        self.tiempo = QtCore.QTimer()
        self.tiempo.timeout.connect(self.contarSeg)


        ################################################################################

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5

        #################################################################################

        self.segundos = 0
        self.enemigos = []
        self.jugador = [0, 0]
        self.enemigos_vivos = 0

        ##############################################

        self.limpiar()

    # Área de los Slots
    def keyPressEvent(self, event):
        Xusr = self.jugador[0]
        Yusr = self.jugador[1]
        if event.key() == Qt.Key_W:
            if Yusr + 1 <= self.yMax:
                self.jugador[1] = Yusr + 1
            else:
                self.jugador[1] = self.yMin
        if event.key() == Qt.Key_A:
            if Xusr - 1 >= self.xMin:
                self.jugador[0] = Xusr - 1
            else:
                self.jugador[0] = self.xMax
        if event.key() == Qt.Key_S:
            if Yusr - 1 >= self.yMin:
                self.jugador[1] = Yusr - 1
            else:
                self.jugador[1] = self.yMax
        if event.key() == Qt.Key_D:
            if Xusr + 1 <= self.xMax:
                self.jugador[0] = Xusr + 1
            else:
                self.jugador[0] = self.xMin

        for enemigo in self.enemigos:
            if self.jugador[0] == enemigo[0] and self.jugador[1] == enemigo[1]:
                self.enemigos.pop(self.enemigos.index(enemigo))
                self.enemigos_vivos -= 1
                self.lbEnemigos.setText("Enemigos: "+str(self.enemigos_vivos))

        self.limpiar()
        self.graficar()

    def contarSeg(self):
        self.segundos += 1
        self.lbTiempo.setText("Tiempo: "+str(self.segundos))

    def mover(self):
        n = self.sender().objectName()
        Xusr = self.jugador[0]
        Yusr = self.jugador[1]

        if n == "btn_arriba":
            if Yusr + 1 <= self.yMax:
                self.jugador[1] = Yusr + 1
            else:
                self.jugador[1] = self.yMin
        elif n == "btn_abajo":
            if Yusr - 1 >= self.yMin:
                self.jugador[1] = Yusr - 1
            else:
                self.jugador[1] = self.yMax
        elif n == "btn_izquierda":
            if Xusr - 1 >= self.xMin:
                self.jugador[0] = Xusr - 1
            else:
                self.jugador[0] = self.xMax
        elif n == "btn_derecha":
            if Xusr + 1 <= self.xMax:
                self.jugador[0] = Xusr + 1
            else:
                self.jugador[0] = self.xMin
        elif n == "btn_centro":
            self.jugador[0] = 0
            self.jugador[1] = 0

        for enemigo in self.enemigos:
            if self.jugador[0] == enemigo[0] and self.jugador[1] == enemigo[1]:
                self.enemigos.pop(self.enemigos.index(enemigo))
                self.enemigos_vivos -= 1
                self.lbEnemigos.setText("Enemigos: "+str(self.enemigos_vivos))

        self.limpiar()
        self.graficar()

    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.tiempo.start(500)
            self.btn_action.setText("DETENER")

            self.jugador = [0, 0]  # vuelve al jugar al centro
            self.enemigos_vivos = rnd.randrange(1, 10)
            self.lbEnemigos.setText("Enemigos: "+str(self.enemigos_vivos))

            # Enemigos
            totalEnemigos = self.enemigos_vivos
            self.enemigos = []
            while totalEnemigos > 0:
                newE = [rnd.randrange(self.xMin+1, self.xMax-1),
                        rnd.randrange(self.yMin+1, self.yMax-1)]
                dup = False
                if newE[0] == self.jugador[0] and newE[1] == self.jugador[1]:
                    dup = True
                else:
                    for enemigo in self.enemigos:
                        if enemigo[0] == newE[0] and enemigo[1] == newE[1]:
                            dup = True
                            break
                if not dup:
                    self.enemigos.append(newE)
                    totalEnemigos -= 1
            self.graficar()
        else:
            self.btn_action.setText("INICIAR")
            self.limpiar()
            self.tiempo.stop()
            self.segundos = 0
            self.lbTiempo.setText("Tiempo: "+str(self.segundos))
            self.lbEnemigos.setText("Enemigos: 0")

    def limpiar(self):
        plt.cla()  # BORRA_TODO EL GRAFICO

        x = [i for i in range(self.xMin, self.xMax + 1)]  # GENERA LOS TICKS
        y = [i for i in range(self.yMin, self.yMax + 1)]  # GENERA LOS TICKS

        self.ax.set_xticks(x)
        self.ax.set_yticks(y)

        #self.ax.set_axis_off()

        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)
        #plt.grid(True)  #CUADRICULA - No me justo como se ve :p

        self.canvas.draw()  # DIBUJAR EL GRAFICO

    def graficar(self):
        # POSICIONA AL USUARIO EN LA GRAFICA
        self.ax.plot(self.jugador[0], self.jugador[1],
                     marker="$oωo$",  # o . *  x   1
                     markersize=20,
                     markerfacecolor="black",  # color interno del marcador
                     markeredgewidth=0,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        # POSICIONA A LA COMPUTADORA EN EL GRAFICO
        for enemigo in self.enemigos:
            self.ax.plot(enemigo[0], enemigo[1],
                         marker="$òωó$",  # o . *  x   1
                         markersize=20,
                         markerfacecolor="red",  # color interno del marcador
                         markeredgewidth=0,  # tamaño del borde del marcador
                         markeredgecolor="red",  # color del borde del marcador
                         )

        self.canvas.draw()  # DIBUJA EL GRAFICO

        # COMPRUEBA CADA QUE SE GRAFICA SI EL USUARIO ALCANZO A LA COMPUTADORA
        # SI LAS COORDENADAS DE AMBOS ESTAN EN LA MISMA POSICION, ENTONCES EL USUARIO ALCANZO
        # A LA COMPUTADORA..

        if self.enemigos_vivos == 0:
            self.tiempo.stop()
            m = QtWidgets.QMessageBox()
            m.setText("GANASTE!")
            m.exec_()
            self.action()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())