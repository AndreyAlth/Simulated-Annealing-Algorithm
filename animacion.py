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

    #Se crea una lista vacia
    puntos = []
    #Abrimos el archivo con la funcion open(nombre, modo)
    #donde el parametro nombre es el nombre del archivo
    #el segundo parametro es el modo de abrir el archivo
    # r significa de read, solo abrimos el archivo para leer
    abrir = open(archivo, "r")
    #recorremos cada linea del archivo
    for line in abrir:
        #la funcion split(), divide la linea del archivo cuando
        #cuando encuentre el parametro asignado, regresando una lista
        pareja = line.split(" ")
        #recorremos los valores de la lista parejas
        for valor in range(len(pareja)):
            #convertimos cada valor de string a int
            pareja[valor] = int(pareja[valor])
        #insertamos la lista pareja en la lista puntos
        puntos.append(pareja)
    print(puntos)
    return []

obtenerPuntos("puntos.txt")
