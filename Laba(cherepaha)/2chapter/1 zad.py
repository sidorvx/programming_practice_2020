import turtle
from random import *
turtle.shape('turtle')
turtle.width(3)
turtle.color('red')
n = randint(30, 60)
for i in range(n):
    a = randint(0, 100)
    b = randint(0, 360)
    turtle.forward(a)
    turtle.left(b)