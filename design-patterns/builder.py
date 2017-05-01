""" Demonstrates builder pattern """

class Director():
    """Director"""

    def __init__(self, builder):
        """ Houses concrete builder """
        self._builder = builder

    def construct_car(self):
        """ Constructs a car using builder """
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        """ Returns car contained in builder """
        return self._builder.car

class Builder():
    """Abstract Builder"""

    def __init__(self):
        """ Initializes car attribute """
        self.car = None

    def create_new_car(self):
        """ Creates new car and assigns to attribute """
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        """ Updates car model """
        self.car.model = "Skylark"

    def add_tires(self):
        """ Updates car tires """
        self.car.tires = "Regular tires"

    def add_engine(self):
        """ Updates car engine """
        self.car.engine = "Turbo engine"


class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


# Construct a car using the builder pattern
BUILDER = SkyLarkBuilder()
DIRECTOR = Director(BUILDER)
DIRECTOR.construct_car()
CAR = DIRECTOR.get_car()
print(CAR)
