""" Demonstrates bridge design pattern """

class DrawingAPIOne(object):
    """ Implementation-specific abstraction version 1 """

    def draw_circle(self, x_coord, y_coord, radius):
        """ Defines how API 1 implements drawing circles """
        print("API 1 drawing a circle at {}, {} with radius {}!".format(x_coord, y_coord, radius))


class DrawingAPITwo(object):
    """ Implementation-specific abstraction version 2 """

    def draw_circle(self, x_coord, y_coord, radius):
        """ Defines how API 2 implements drawing circles """
        print("API 2 drawing a circle at {}, {} with radius {}!".format(x_coord, y_coord, radius))


class Circle(object):
    """ Implementation dependent abstraction """

    def __init__(self, x_coord, y_coord, radius, drawing_api):
        """ Initializes the necessary attributes """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation specific abstraction taken care of by another class: DrawingAPI """
        self._drawing_api.draw_circle(self._x_coord, self._y_coord, self._radius)

    def scale(self, percent):
        """ Implementation independent """
        self._radius *= percent


# Build and draw first circle using API1
CIRCLE1 = Circle(1, 2, 3, DrawingAPIOne())
CIRCLE1.draw()

# Build and draw another circle using API2
CIRCLE2 = Circle(2, 3, 4, DrawingAPITwo())
CIRCLE2.draw()
