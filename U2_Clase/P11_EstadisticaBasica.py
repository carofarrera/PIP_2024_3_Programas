import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P11_EstadisticaBasica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_promedio.clicked.connect(self.estadistica)
        ###
        ###
        ###

    # Área de los Slots
    def estadistica(self):
        lista = self.txt_A.text() ## 10, 20, 30, 40
        print(lista)
        numeros = lista.split(",") ##numero en cadena de caracteres
        print(numeros)
        numeros = [int(i) for i in numeros]
        print(numeros)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())