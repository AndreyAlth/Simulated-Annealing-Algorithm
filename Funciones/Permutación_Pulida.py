from random import shuffle
def permutacion_aleatoria(n):
        x = [i for i in range(0,n)]
        shuffle(x)
        return x
