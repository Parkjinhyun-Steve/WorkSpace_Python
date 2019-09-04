import turtle as t

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x, y):
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("red")
    square(50)
    t.color("yellow")
    t.end_fill()

s = t.Screen()  
s.onscreenclick(drawit)  
