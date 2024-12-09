import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_IntroPushButton.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        try:
            self.btn_saludar.clicked.connect(self.saludar)
        except Exception as error:
            print(error)

    # Área de los Slots
    def saludar(self):
        cadena = "Hola"
        self.mensaje(cadena)

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())