import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P25_SeleccionOpciones_Sender.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.rb_soltero.clicked.connect(self.soltero)
        #self.rb_casado.clicked.connect(self.casado)
        #self.rb_union.clicked.connect(self.union)

        self.rb_soltero.toggled.connect(self.estado.civil)
        self.rb_casado.toggled.connect(self.estado.civil)
        self.rb_union_libre.toggled.connect(self.estado.civil)

        self.rb_perro.toggled.connect(self.mascota)
        self.rb_gato.toggled.connect(self.mascota)
        self.rb_hamster.toggled.connect(self.mascota)

    # Área de los Slots
    def estado_civil(self):
        objeto = self.sender()
        nombre_objeto = objeto.objectName()

        nombre_objeto = nombre_objeto.split("_")
        nombre_objeto = " ".join(nombre_objeto[1:])
        print(nombre_objecto, end=" ")
        check = objecto.isChecked()
        if check:
            print(" seleccionado")
        else:
            print("desmarcado")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())