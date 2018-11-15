import turtle
from turtle import *

def dibujar_puntos(start, pts):

    screensize(800, 800) #screensize define el tamaño de pantalla que se utilizará para la animación
    t = Turtle()
    t.color('gray')#color de la línea
    t.pensize(2)#tamaño de la línea en px


    t.penup()
    t.goto(start) #punto de partida de la línea
    t.dot('black') #define la marca de un punto en el start además de agregarle color


    t.pendown()
    x, y = start #se define x y como coordenadas para punto de patida "start"

    for p in pts:
        dx, dy = p
        t.goto(x + dx, y + dy)  #define la dirección que tomará la línea
        t.dot('black') #define el agregar un punto en cada punto marcado además de definir el color

    t.penup()

puntos = [[239, 235], [-128, 42], [-242, -5], [-93, 77], [-114, -237], [-83, -131], [-270, 171], [-221, 53], [122, 35], [53, -106], [-81, 236], [-105, -296], [-109, -285], [-116, -6], [-52, -184], [144, -102], [-241, 72], [111, -91], [-56, 277], [-206, 200], [-70, -173], [-82, 111], [30, -130], [-230, -265], [153, 299], [24, -61], [244, -36], [-234, -275], [-159, -242], [-298, 213], [281, -165], [132, -125], [252, 83], [54, -60], [-211, -231], [-253, 105], [82, -133], [268, -228], [-42, 54], [-201, 25], [276, -262], [110, -197], [23, 193], [-251, -127], [-295, -277], [-129, 49], [-232, -265], [-205, -156], [-199, 214], [151, -107]]
#puntos obtenidos de la función "obtener_puntos"
dibujar_puntos(start=(0, 0) , pts=puntos )
