import turtle

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

#print(obtenerPuntos("puntos.txt"))
