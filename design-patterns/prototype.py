""" Demonstrates protoype design pattern """

import copy

class Prototype:
    """ Prototype class """

    def __init__(self):
        """ Initialises holder for objects """
        self._objects = {}

    def register_object(self, name, obj):
        """ Register an object """
        self._objects[name] = obj

    def unregister_object(self, name):
        """ Unregisters an object """
        del self._objects[name]

    def clone(self, name, **attr):
        """ Clone a registered object and update its attributes """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    """ Car class """

    def __init__(self):
        self.name = "Skylark"
        self.color = "Blue"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)

# Creates prototypical instance and clones it
C = Car()
PROTO = Prototype()
PROTO.register_object('skylark', C)

C1 = PROTO.clone('skylark')
print(C1)

