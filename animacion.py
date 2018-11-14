import turtle
import math

def animacion(puntos, soluciones):
    '''
    Usar la tortuga para dibujar
    1) La lista de puntos (en negro)
    2) La solucion inicial (en gris)
    3) La solucion final (en verde)

    :param puntos: Lista de puntos a dibujar
    :param soluciones: Lista de soluciones a modificar
    :return: None
    '''
    return None


def obtenerPuntos(archivo):
    '''
    Abrir un archivo con lista de puntos x,y uno por linea y regresa
    una matriz de puntos
    :param archivo: Nombre del arcbivo
    :return: La lista de puntos
    '''

    puntos = []
    abrir = open(archivo, "r")
    for line in abrir:
        mitad = math.floor((len(line))/2)
        print(mitad)
    print(puntos)
    return []

obtenerPuntos("puntos.txt")
