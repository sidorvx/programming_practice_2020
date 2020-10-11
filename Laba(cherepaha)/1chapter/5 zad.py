import turtle
n = 10
a = 20
turtle.shape('turtle')
for i in range(n):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.right(135)
    turtle.penup()
    turtle.forward(8)
    a += 12
    turtle.left(135)
    turtle.pendown()

