import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P4_DatosDeImagenes_Completo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.lista_imagenes = {

            1: ":/logo/1.jpg",
            2: ":/elefante/elefante.jpg",
            3: ":/playa/playa.jpg"

        }
        self.datos_imagenes = {

            1: ["Carolina", "25 años", "estudiante", "ver la tele"],
            2: ["Dilan", "21 años", "estudiante", "estar en el celular"],
            3: ["Jeremy", "21 años", "estudiante", "ir a robotica"],

        }
        self.clave_imagen = 1
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
        self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
        self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
        self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

    # Área de los Slots
    def atras(self):
        print(self.clave_imagen)
        if self.clave_imagen >= 2:
            self.clave_imagen -= 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

    def adelante(self):
        print(self.clave_imagen)
        if self.clave_imagen < 3:
            self.clave_imagen += 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())