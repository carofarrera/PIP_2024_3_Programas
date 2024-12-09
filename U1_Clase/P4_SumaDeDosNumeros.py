import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P4_SumaDeDosNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        try:
            self.btn_sumar.clicked.connect(self.sumar)
        except Exception as error:
            print(error)

    # Área de los Slots
    def sumar(self):
        numero1 =  self.txt_numero1.text() #str
        numero2 =  self.txt_numero2.text() #str

        numero1 = int(numero1)
        numero2 = int(numero2)

        resultado = numero1 + numero2

        self.mensaje("La suma es: "+str(resultado))



    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())