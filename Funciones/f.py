#Calcular el valor de la solución actual

def f(puntos,x):
    parejas = x
    for i in range(parejas):
        resta_al_cuadrado_a = (puntos[i+1][0] - puntos[i][0]) ** 2
        resta_al_cuadrado_b = (puntos[i+1][1] - puntos[i][1]) ** 2
        suma = resta_al_cuadrado_a + resta_al_cuadrado_b
        distancia = suma**0.5
        DistanciaT += distancia
    return DistanciaT
