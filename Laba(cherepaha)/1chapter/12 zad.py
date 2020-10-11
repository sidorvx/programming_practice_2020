import turtle


def circle(radius):
    for i in range(72):
        t.forward(radius)
        t.right(2.5)


t = turtle.Turtle()
t.left(180)
t.penup()
t.forward(200)
t.right(90)
t.pendown()
for i in range(5):
    for j in range(1, 3):
        rad = 2.5 if (j + 1) % 2 == 0 else 2.5 / 4
        circle(rad)
