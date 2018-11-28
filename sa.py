from Funciones.funciones import *
from progress.bar import Bar

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
    bar = Bar('Procesandoooo', max=iteraciones)
    solucion = []
    x = permutacion_aleatoria(n)
    solucion.append(x)
    f_x = f(puntos,x)
    valormenor = f_x
    temp = t_ini
    print("datos iniciales")
    print("temp ", temp)
    print("distancia ", f_x)
    print("solucion primera ", solucion[0])
    for i in range(iteraciones):
        bar.next()
        x_ = modifica(x,n)
        f_x_ = f(puntos,x_)
        if cambio(f_x, f_x_, temp):
            x = x_
            f_x = f_x_
        temp = actualiza_temp(t_ini,t_fin,i,iteraciones)

    solucion.append(x)
    print("datos finales")
    print("temp ", temp)
    print("distancia final fue ", f_x)
    print("solucion final ", solucion[1])
    return solucion
