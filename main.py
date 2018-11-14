

from sa import *

from animacion import *

puntos = obtenerPuntos('lista.txt')
soluciones = enfriamiento_simulado(puntos, 10000, 10, 0.1, len(puntos))
animacion(puntos, soluciones)