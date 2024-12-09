import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P26_Combobox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.dicc_alumno = {
            "2206":["Fernando","IN","20"],
            "REP01":["Sebastian","ISC",22],
            "MACI2":["Maciel","IC",21],
            "CAROL":["Carolina","ISC",24]
        }
        self.cb_alumnos.addItem("Fernando", "2206")
        self.cb_alumnos.addItem("Sebastian", "REP01")
        self.cb_alumnos.addItem("Maciel", "MACI2")
        self.cb_alumnos.addItem("Carolina","CAROL")
    # Área de los Slots
    #tres formas de acceder a los elementos de un combobox...
    #texto - es lo que ve el usaurio
    #data-clave
    #indice
        self.cb_alumnos.currentIndexChanged.connect(self.cambiaIndice)

    def cambiaIndice(self):
        texto = self.cb_alumnos.currentText()
        data = self.cb_alumnos.currentData()
        indice = self.cb_alumnos.currentIndex()
        print(texto + " - " + data + " - " + str(indice))
        self.cargaDatos(data)

    def cargaDatos(self, clave):
        alumno = self.dicc_alumno[clave]
        self.txt_nombre.setText(alumno[0])
        self.txt_carrera.setText(alumno[1])
        self.txt_edad.setText(str(alumno[2]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())