import turtle
from turtle import *
import time

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
    #puntos en negro
    screensize(800, 800)
    t = Turtle()
    t.hideturtle()
    t.speed(15)
    t.pensize(7)
    t.penup()
    for p in puntos:
        dx, dy = p
        t.goto(dx, dy)
        t.pendown()
        t.dot('red')
        t.penup()
    time.sleep(2)
    t.showturtle()

    #TRAZA LAS SOLUCIONES
    for r in range(len(soluciones)):
        t.penup()
        if(r == 0):
            t.speed(8)
            t.pensize(1)
            t.color('gray')
        elif(r == 1):
            t.speed(5)
            t.pensize(4)
            t.color('green')
        for p in soluciones[r]:
            dx, dy = puntos[p]
            t.goto(dx, dy)
            t.pendown()
        time.sleep(5)
    return None


def obtenerPuntos(archivo):
    '''
    Abrir un archivo con lista de puntos x,y uno por linea y regresa
    una matriz de puntos
    :param archivo: Nombre del archivo
    :return: La lista de puntos
    '''
    puntos = []
    txt=open(archivo,'r')
    leer_fila= txt.readlines()
    txt.close()
    indice = 0
    for lista in leer_fila:
      parte = lista.split()
      puntos.append([])
      px = int(parte[0])
      py = int(parte[1])
      puntos[indice].append(px)
      puntos[indice].append(py)
      indice+=1
    return puntos
