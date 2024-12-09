import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P6_PromedioCalificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        try:
            self.btn_calcular.clicked.connect(self.calcular)
        except Exception as error:
            print(error)

    # Área de los Slots
    def calcular(self):
        calificaciones =  self.txt_calificaciones.text() #str

        #CONVIERTE LA CADENA DE CARACTERES EN UNA LISTA DE CADENAS
        lista_calificaciones = calificaciones.split(" ")

        #CONVIERTE LA LISTA DE CADENAS EN LISTA DE NUMEROS
        lista_calificaciones = [int(i) for i in lista_calificaciones]

        resultado = sum(lista_calificaciones)/len(lista_calificaciones)

        self.txt_resultado.setText(str(resultado))



    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())