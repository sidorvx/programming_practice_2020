import turtle
t = turtle.Turtle()


def circle(rad, arc=None):
    if arc is not None:
        iterat = 18
        fi = -10
    else:
        iterat = 36
        fi = 10
    for i in range(iterat):
        t.left(fi)
        t.forward(rad)


t.begin_fill()
circle(20)
t.color('yellow')
t.end_fill()
t.color('black')
t.penup()
# правый глаз
t.goto(50, 140)
t.pendown()
t.begin_fill()
circle(5)
t.color('red')
t.end_fill()
t.color('black')
t.penup()
# левый глаз
t.goto(-55, 140)
t.pendown()
t.begin_fill()
circle(5)
t.color('red')
t.end_fill()
t.color('black')
t.penup()
# нос
t.goto(0, 120)
t.pendown()
t.width(10)
t.right(90)
t.forward(30)
t.penup()
# рот
t.goto(65, 90)
t.color('brown')
t.pendown()
circle(12, arc='Yes')
