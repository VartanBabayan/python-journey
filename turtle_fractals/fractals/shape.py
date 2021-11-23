from abc import ABC, abstractmethod


class ShapeCreator(ABC):
    def __init__(self, turtle):
        self.t = turtle

    @abstractmethod
    def configureTurtle(self, pencolor, fillcolor, pensize, speed, shapesize):
        raise NotImplementedError()
