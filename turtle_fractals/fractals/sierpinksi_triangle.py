from turtle import title
from .shape import ShapeCreator


class SierpinskiTriangle(ShapeCreator):
    def __init__(self, turtle):
        super().__init__(turtle)
        title("Sierpinski's Triangle")
        self.configureTurtle("black", "red", 1, 4, 1)

    def configureTurtle(self, pencolor, fillcolor, pensize, speed, shapesize):
        self.t.pen(pencolor=pencolor, fillcolor=fillcolor, pensize=pensize, speed=speed)
        self.t.shapesize(shapesize, shapesize, shapesize)

    def Sierpinski(self, size, order):
        t = self.t

        if order == 0:
            t.stamp()
        else:
            for i in range(0, 3):
                t.fd(size)
                self.Sierpinski(size / 2, order - 1)
                t.bk(size)
                t.lt(120)

    def drawSierpinski(self):
        t = self.t

        t.shape("triangle")
        t.rt(30)
        t.pu()
        t.ht()
        self.Sierpinski(200, 3)
        t.reset()
        t.clear()
