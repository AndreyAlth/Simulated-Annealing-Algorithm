from sa import *
from Funciones.funciones import *
from animacion import *
puntos = obtenerPuntos('puntos.txt')
soluciones = enfriamiento_simulado(puntos, 100000, 10, 0.1, len(puntos))
animacion(puntos, soluciones)
