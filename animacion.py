import turtle
from turtle import *
import time

def animacion(puntos, soluciones):
    """ 1) DIBUJA LOS PUNTOS EN NEGRO"""
    screensize(800, 800) #screensize define el tamaño de pantalla que se utilizará para la animación
    t = Turtle() #crea la tortuga
    t.hideturtle() #esconde la tortuga
    t.speed(10) #velocidad de la tortuga
    t.pensize(4)#tamaño de la línea en px
    t.penup() #levanta el lapiz
    for p in puntos: #ciclo hasta fin de puntos
        dx, dy = p #asigna variable a puntos
        t.goto(dx, dy)  #define las coordenadas de aparicion
        t.pendown() #escribe
        t.dot('black') #define el agregar un punto en cada punto marcado además de definir el color
        t.penup() #levanta el lapiz
    time.sleep(2) #espera 2s

    """ 2) TRAZA LA SOLUCION INICIAL EN GRIS (agregar primera permutacion)"""
    t.showturtle() #muestra la tortuga
    t.speed(4) #velocidad de la tortuga
    t.pensize(3)#tamaño de la línea en px
    t.color('gray')#color de la tortuga
    t.penup() #levanta el lapiz
    for p in puntos: #ciclo hasta fin de puntos
        dx, dy = p #asigna variable a puntos
        t.goto(dx, dy)  #define la dirección que tomará la línea
        t.pendown() #escribe
    t.penup() #levanta el lapiz
    time.sleep(10) #espera 10s

    """ 3) TRAZA LA SOLUCION FINAL EN VERDE
    pix, piy = 0 #sin asignar nada por el momento
    t.goto(pix, piy) #punto incial
    t.speed(4) #velocidad de la tortuga
    t.pensize(2)#tamaño de la línea en px
    t.color('green')#color de la tortuga
    t.penup() #levanta el lapiz
    for p in soluciones: #ciclo hasta fin de puntos
        dx, dy = p #asigna variable a puntos
        t.goto(dx, dy)  #define la dirección que tomará la línea
        t.pendown() #escribe
    t.penup() #levanta el lapiz
    time.sleep(10) #espera 10s
    """

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
    :param archivo: Nombre del archivo
    :return: La lista de puntos
    '''
    puntos = []  #matriz a devolver
    txt=open(archivo,'r')  #formato de apertura el archivo
    leer_fila= txt.readlines() #lee por lineas
    txt.close() #cierra el archivo
    indice = 0 #posicion inicial de la matriz donde se guardaran los puntos
    for lista in leer_fila:  #ciclo de lectura por linea
      parte = lista.split()  #separa el archivo por espacios
      puntos.append([])  #agrega la caja donde ira x y
      px = int(parte[0])  #convierte el string x a entero
      py = int(parte[1])  #convierte el string y a entero
      puntos[indice].append(px)  #agrega px dentro de la cja
      puntos[indice].append(py)  #agrega py dentro de la caja
      indice+=1   #incremente el indice de la matriz
    return puntos

#ejem print(obtenerPuntos("puntos.txt"))
