from random import shuffle, random, sample
from math import exp
from numpy import geomspace

def permutacion_aleatoria(n):
    '''
    Crea una permutacion de 1 a n aleatoria
    :param n:
    :return:
    '''
    x = [p for p in range(0,n)]
    shuffle(x)
    return x

def f(puntos,x):
    '''
    Calcula el valor de la solucion actual
    :param puntos:
    :param x:
    :return:
    '''
    distanciaT = 0
    for i in range(len(x)-1):
        distanciaT += ((puntos[x[i]][0]-puntos[x[i+1]][0])**2+(puntos[x[i]][1]-puntos[x[i+1]][1])**2)**0.5
    return distanciaT

def modifica(x,n):
    '''
    Modifica la solucion actual haciendo un swap
    :param x:
    :param n:
    :return:
    '''
    n_orden = list(x)
    [i,j] = sorted(sample(range(n),2));
    n_orden =  n_orden[:i] + n_orden[j:j+1] +  n_orden[i+1:j] + n_orden[i:i+1] + n_orden[j+1:]
    return n_orden

def cambio(f_x, f_x_, temp):
    '''
    Determina si se cambia la solucion  o se queda
    con la actual
    :param f_x: El valor de la solucion actual
    :param f_x_: El valor de la solucion nueva
    :param temp: Temperatura actual
    :return: Verdadero si se cambia, Falso si no
    '''
    d = (f_x)-(f_x_) #si esto es positivo p siempre sera > 1
    radd = random()
    p = exp( d / temp)
    if p > radd:
        return True
    else:
        return False

def actualiza_temp(t_ini,t_fin,i,iter):
    '''
    Actualiza la temperatura
    :param t_ini: Temp inicial
    :param t_fin: Temp final
    :param i: iteracion actual
    :return: Nueva temperatura
    '''
    k = (i+1)*(-1)
    N_temperatura = geomspace(t_fin,t_ini,iter)[k] #va alrevez
    return N_temperatura
