import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P1_MensajeEmergente.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        cadena = "Hola!"
        self.mensaje(cadena)
        # Área de los Signals
    def mensaje(self,texto):
            m = QtWidgets.QMessageBox()
            m.setText(texto)
            m.exec()

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())