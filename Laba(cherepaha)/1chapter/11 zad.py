import turtle


def polar(angle):
    for j in range(360):
        t.left(angle)
        t.forward(1+i/4)


t = turtle.Turtle()
t.left(90)
for i in range(0, 9):
    for j in range(1,3):
        polar((-1)**(j+1))
