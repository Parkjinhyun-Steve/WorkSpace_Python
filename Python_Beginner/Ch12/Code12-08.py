import turtle
import random

##
class Shape:
    myTrutle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTrutle = turtle.Turtle('turtle')

    def setPen(Self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTrutle.pensize(pSize)
    
    def drawShape(self):
        pass

class Rectangle(Shape):
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        ##
        sx1, sy1, sx2, sy2 = [0] * 4

        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2

        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()
        self.myTrutle.penup()
        self.myTrutle.goto(sx1, sy1)
        self.myTrutle.pendown()
        self.myTrutle.goto(sx1, sy2)
        self.myTrutle.goto(sx2, sy2)
        self.myTrutle.goto(sx2, sy1)
        self.myTrutle.goto(sx1, sy1)

def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()

##
turtle.title('T')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
