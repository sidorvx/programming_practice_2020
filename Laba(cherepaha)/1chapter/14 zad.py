import turtle
t = turtle.Turtle()
n = int(input())


def star(n):
    t.left(180 - (180 / n))
    t.forward(200)
    

for i in range(n):
    star(n)
