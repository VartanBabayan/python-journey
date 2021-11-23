from turtle import title
from .shape import ShapeCreator


class FractarSquare(ShapeCreator):
    def __init__(self, turtle):
        super().__init__(turtle)
        title("Turtle Square")
        self.configureTurtle("black", "red", 1, 2, 2)

    def configureTurtle(self, pencolor, fillcolor, pensize, speed, shapesize):
        self.t.pen(pencolor=pencolor, fillcolor=fillcolor, pensize=pensize, speed=speed)
        self.t.shapesize(shapesize, shapesize, shapesize)

    def drawSquare(self):
        t = self.t
        t.begin_fill()

        length = 200
        angle = 90
        for i in range(4):
            t.fd(length)
            t.rt(angle)

        t.end_fill()
        t.clear()

    def drawFractalSquare(self):
        t = self.t
        length = 200
        angle = 90
        variance = 20
        reducer = 1.4142

        for i in range(4):
            t.fd(length)
            t.rt(angle)

        t.rt(angle)
        t.fd(length)
        t.lt(angle)
        while length > 0 and variance > 0:
            length -= variance

            if variance < 10:
                reducer = 0.5

            variance -= reducer
            for i in range(4):
                t.fd(length)
                t.lt(angle)

        t.reset()
        t.clear()
