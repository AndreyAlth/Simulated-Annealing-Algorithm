import random, numpy, math, copy, matplotlib.pyplot as plt
from animacion import *
from random import shuffle, randint, uniform
import turtle
from turtle import *
import time
from progress.bar import Bar
iteraciones = 100000
bar = Bar('Procesandoooo', max=iteraciones)
ct = obtenerPuntos('puntos.txt')
n = len(ct)
tr = random.sample(range(n),n);
bt= 0

for i in range(n-1):
    bt += ((ct[tr[i]][0]-ct[tr[i+1]][0])**2+(ct[tr[i]][1]-ct[tr[i+1]][1])**2)**0.5

def nC(p, l, k):
    nc = 0
    for i in range(k-1):
        nc += ((p[l[i]][0]-p[l[i+1]][0])**2+(p[l[i]][1]-p[l[i+1]][1])**2)**0.5
    return nc

def nT(k, d):
    l = list(d)
    [i,j] = sorted(random.sample(range(k),2));
    nt =  l[:i] + l[j:j+1] +  l[i+1:j] + l[i:i+1] + l[j+1:]
    return nt

def aceptacion(bc, nc, tr, ntr, tp):
    d = bc-nc #si esto es positivo p siempre sera > 1
    radd = random.random()
    p = math.exp( d / tp)
    if p > radd:
        tr = list(ntr)
        bc = nc
    return tr, bc

for temperature in numpy.logspace(0,5,num=iteraciones)[::-1]:
    bar.next()
    nt = nT(n, tr)
    nc = nC(ct, nt, n)
    tr, bt = aceptacion(bt, nc, tr, nt, temperature)

print(" ")
print(bt)
plt.plot([ct[tr[i % n]][0] for i in range(n+1)], [ct[tr[i % n]][1] for i in range(n+1)], 'xb-');
plt.show()
screensize(800, 800)
t = Turtle()
t.hideturtle()
t.speed(15)
t.pensize(7)
t.penup()
for p in tr:
    dx, dy = ct[p]
    t.goto(dx, dy)
    t.pendown()
    t.dot('red')
    t.penup()
time.sleep(2)
t.showturtle()
t.penup()
t.speed(5)
t.pensize(4)
t.color('green')
for p in tr:
    dx, dy = ct[p]
    t.goto(dx, dy)
    t.pendown()
dx, dy = ct[tr[0]]
t.goto(dx, dy)
time.sleep(5)
