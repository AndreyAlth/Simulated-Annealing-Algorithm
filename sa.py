
from funciones import *


def enfriamiento_simulado(puntos, iteraciones, t_ini, t_fin, n):
    '''
    Implementa el algoritmo de enfriamiento simulado para el problema
    del cartero
    :param puntos: Los puntos a visitar
    :param iteraciones: Cuantas iteraciones va a correr el algoritmo
    :param t_ini: Temperatura ininicial
    :param t_fin: Temperatura final
    :param n: Numero de ciudades
    :return: Regresa en un arreglo, la permutacion inicial, y la permutacion final
    '''
    solucion = []
    x = permutacion_aleatoria(n)
    solucion.append(x)
    f_x = f(puntos,x,n)
    temp = t_ini
    for i in range(iteraciones):
        x_ = modifica(x,n)
        f_x_ = f(puntos,x_,n)
        if cambio(f_x, f_x_, temp):
            x = x_
            f_x = f_x_
        temp = actualiza_temp(t_ini,t_fin,i)
    solucion.append(x)
    return solucion