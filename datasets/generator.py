global str
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Generate Data
l = 90
maxCantAlmacen = 99
puntosAlmacen = []
puntosEntrega = []
puntosNeutros = []
for x in range(0, l):
  for y in range(0, l):
    ran = np.random.randint(0,10)
    if ran == 0:
      pointA = (x-1, y)
      pointB = (x, y-1)
      pointC = (x-1, y-1)
      pointD = (x+1, y-1)
      if pointA in puntosAlmacen or pointB in puntosAlmacen or pointC in puntosAlmacen or pointD in puntosAlmacen:
        if len(puntosAlmacen) <= maxCantAlmacen:
          puntosAlmacen.append((x, y))
        else:
          puntosEntrega.append((x, y))
      else:
        if len(puntosAlmacen) <= maxCantAlmacen:
          puntosAlmacen.append((x, y))
        else:
          puntosEntrega.append((x, y))
    elif ran == 1:
      puntosEntrega.append((x, y))
    elif ran == 2:
      puntosEntrega.append((x, y))
    elif ran == 3:
      puntosEntrega.append((x, y))
    elif ran == 4:
      puntosEntrega.append((x, y))
    elif ran == 5:
      puntosEntrega.append((x, y))
    elif ran == 6:
      puntosEntrega.append((x, y))
    elif ran == 7:
      puntosNeutros.append((x, y))
    elif ran == 8:
      puntosNeutros.append((x, y))
    elif ran == 9:
      puntosNeutros.append((x, y))

# Print data in console
print("Puntos de Almacenes:" + str(puntosAlmacen))
print("Puntos de Entrega:" + str(puntosEntrega))

# Export data
np.savetxt("almacenes.csv", puntosAlmacen, fmt='%i', delimiter=",")
np.savetxt("puntos_entrega.csv", puntosEntrega,fmt='%i', delimiter=",")

# Data for plot
plt.figure(figsize=(10,10))
pxDistr = list(map(lambda x: x[0], puntosAlmacen)) 
pyDistr = list(map(lambda x: x[1], puntosAlmacen)) 
pxEntre = list(map(lambda x: x[0], puntosEntrega)) 
pyEntre = list(map(lambda x: x[1], puntosEntrega)) 
pxNeutro = list(map(lambda x: x[0], puntosNeutros)) 
pyNeutro = list(map(lambda x: x[1], puntosNeutros)) 
# Setup UI
plt.scatter(pxDistr,pyDistr,s=50,color="red",label="Zona de Almacen. " + str(len(puntosAlmacen)))
plt.scatter(pxEntre,pyEntre,s=50,color="blue", label="Zona de entrega. " + str(len(puntosEntrega)))
plt.scatter(pxNeutro,pyNeutro,s=50,color="green", label="Zona Neutra. " + str(len(puntosNeutros)))
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.legend()
# Show 
plt.show()