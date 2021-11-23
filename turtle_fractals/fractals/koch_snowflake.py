from turtle import title
from .shape import ShapeCreator


class Kochsnowflake(ShapeCreator):
    def __init__(self, turtle):
        super().__init__(turtle)
        title("Sierpinski's Triangle")
        self.configureTurtle("black", "red", 2, 2, 2)

    def configureTurtle(self, pencolor, fillcolor, pensize, speed, shapesize):
        self.t.pen(pencolor=pencolor, fillcolor=fillcolor, pensize=pensize, speed=speed)
        self.t.shapesize(shapesize, shapesize, shapesize)

    def KochSnowflake(self, size, level):
        if level == 0:
            self.t.forward(size)
        else:
            self.KochSnowflake(size / 3, level - 1)
            self.t.left(60)
            self.KochSnowflake(size / 3, level - 1)
            self.t.right(120)
            self.KochSnowflake(size / 3, level - 1)
            self.t.left(60)
            self.KochSnowflake(size / 3, level - 1)

    def drawKochSnowflake(self):
        t = self.t
        size = 300
        level = 2
        for i in range(3):
            self.KochSnowflake(size, level)
            self.t.right(120)

        t.reset()
        t.clear()
