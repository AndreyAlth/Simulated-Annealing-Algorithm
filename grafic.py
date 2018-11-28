import random, numpy, math, copy, matplotlib.pyplot as plt
from animacion import *
from random import shuffle, randint, uniform
import turtle
from turtle import *
import time
cities = obtenerPuntos('puntos.txt')
n = len(cities)
tour = random.sample(range(n),n);
print(tour)
bestcost= 0

for i in range(n-1):
    bestcost += ((cities[tour[i]][0]-cities[tour[i+1]][0])**2+(cities[tour[i]][1]-cities[tour[i+1]][1])**2)**0.5

def newC(p, l, k):
    newc = 0
    for i in range(k-1):
        newc += ((p[l[i]][0]-p[l[i+1]][0])**2+(p[l[i]][1]-p[l[i+1]][1])**2)**0.5
    return newc

def newT(k, d):
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

for temperature in numpy.logspace(0,5,num=10000)[::-1]:
    newtour = newT(n, tour)
    newcost = newC(cities, newtour, n)
    tour, bestcost = aceptacion(bestcost, newcost, tour, newtour, temperature)
print(bestcost)
print(cities)
plt.plot([cities[tour[i % n]][0] for i in range(n+1)], [cities[tour[i % n]][1] for i in range(n+1)], 'xb-');
plt.show()
screensize(800, 800)
t = Turtle()
t.hideturtle()
t.speed(15)
t.pensize(7)
t.penup()
for p in tour:
    dx, dy = cities[p]
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
for p in tour:
    dx, dy = cities[p]
    t.goto(dx, dy)
    t.pendown()
dx, dy = cities[tour[0]]
t.goto(dx, dy)
time.sleep(5)
