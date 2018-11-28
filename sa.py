
from Funciones.funciones import *


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
    f_x = f(puntos,x)
    valormenor = f_x
    temp = t_ini
    print("datos iniciales")
    print("temp ", temp)
    print("distancia ", f_x)
    print("solucion ", solucion[0])
    for i in range(iteraciones):
        x_ = modifica(x,n)
        f_x_ = f(puntos,x_)
        if(f_x_<f_x):
            valormenor = f_x_
        if cambio(f_x, f_x_, temp):
            x = x_
            f_x = f_x_
        temp = actualiza_temp(t_ini,i,iteraciones)

    solucion.append(x)
    print("datos finales")
    print("temp ", temp)
    print("distancia menor de todas fue ", valormenor)
    print("distancia final fue ", f_x)
    print("solucion ", solucion[1])
    return solucion
