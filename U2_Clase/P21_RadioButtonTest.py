import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P21_RadioButtonTest.ui"  # Nombre del archivo aquí.
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
    def validar(self):
        opciones = [
            self.rb_opcionA.isChecked(),
            self.rb_opcionB.isChecked(),
            self.rb_opcionC.isChecked(),
            self.rb_opcionD.isChecked()

        ]
        print(opciones)
        if max(opciones) == 1:
            index = opciones.index(1)
            print(index)
        else:
            print("Debes seleccionar una opción...")

        # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())