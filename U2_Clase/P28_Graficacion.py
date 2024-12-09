archivo = open("../Archivos/datos_sensor_temperatura.csv")

contenido = archivo.readlines()
print(contenido)

datos = [float(i) for i in contenido] #y
print(datos)

x = [i for i in range(1, 16, 1)]

from matplotlib import pyplot as plt
plt.plot(x, datos, marker="o", color="green")
plt.plot(*argsx, datos)
plt.xticks(x)
plt.grid(True)
plt.show()