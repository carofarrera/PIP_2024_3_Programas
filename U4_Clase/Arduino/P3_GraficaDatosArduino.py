
import serial as ser

arduino = ser.Serial(port="COM3", baudrate=9600, timeout=1)

tot_lecturas = int(input("Ingresa el total de lecturas a procesar;"))

lecturas = []
while tot_lecturas>0:
    if arduino.inWaiting():
        cadena = arduino.readLine()
        cadena = cadena.decode().strip()
    if cadena != "":
        print(cadena)
        lecturas.append(int(cadena))
        tot_lecturas -= 1
print("Lecturas obtenidas")