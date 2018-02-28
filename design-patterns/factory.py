""" Factory pattern example """

class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        """ Implements speech """
        return "woof!"


class Cat:
    """ A simple cat class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        """ Implements speech """
        return "meow!"


def get_pet(pet="dog"):
    """ The factory method """

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
