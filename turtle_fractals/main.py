import turtle
import fractals


if __name__ == '__main__':
    t = turtle.Turtle()
    # triangle = fractals.SierpinskiTriangle(t)
    # triangle.drawSierpinski()
    #
    # square = fractals.FractarSquare(t)
    # square.drawSquare()
    # square.drawFractalSquare()

    # t.hideturtle()
    # fern = fractals.BarnsleyFern(t)
    # fern.drawBarnsleyFern()
    # t.showturtle()

    snowflake = fractals.Kochsnowflake(t)
    snowflake.drawKochSnowflake()
