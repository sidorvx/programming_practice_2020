import turtle


def rect(k, s):
    alp = 360 // k
    b = 90 + alp / 2
    turtle.left(b)
    for i in range(k):
        turtle.forward(s)
        turtle.left(360/k)
    turtle.penup()
    turtle.right(b)
    turtle.forward(s/8)
    turtle.pendown()


turtle.shape('turtle')
s = 50

for i in range(3, 14):
    rect(i, s)
    s += s/i**2.5
