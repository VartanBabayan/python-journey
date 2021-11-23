from turtle import RawPen, Screen
import random
from .shape import ShapeCreator


class BarnsleyFern(ShapeCreator):
    def __init__(self, turtle):
        super().__init__(turtle)
        self.configureTurtle("green", "green", 2, 2, 2)

    def configureTurtle(self, pencolor, fillcolor, pensize, speed, shapesize):
        self.t.pen(pencolor=pencolor, fillcolor=fillcolor, pensize=pensize, speed=speed)
        self.t.shapesize(shapesize, shapesize, shapesize)

    def drawBarnsleyFern(self):
        t = self.t
        root = Screen()
        root.setup(width=600, height=800)
        root.title('Barnsley fern')
        root.tracer(n=15000)

        pen = RawPen(root)
        pen.speed(0)
        pen.ht()
        pen.pu()

        dots = 20000
        scale = 50
        foreground = "red"

        x, y = 0.0, 0.0

        for i in range(dots):
            r = random.randint(0, 100)
            if r <= 1:
                tempx = 0.0
                tempy = 0.16 * y
            elif r <= 7:
                tempx = 0.2 * x - 0.26 * y
                tempy = 0.23 * x + 0.22 * y + 1.6
            elif r <= 15:
                tempx = -0.15 * x + 0.28 * y
                tempy = 0.26 * x + 0.24 * y + 0.44
            else:
                tempx = 0.85 * x + 0.04 * y
                tempy = -0.04 * x + 0.850 * y + 1.6
            x, y = tempx, tempy
            pen.setpos(x * scale - scale // 2, y * scale - scale * 3)
            pen.dot(1, foreground)

            t.reset()
            t.clear()
