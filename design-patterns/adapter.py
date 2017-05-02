""" Demonstrates adapter pattern """

class Kenyan:
    """ Kenyan speaker """
    def __init__(self):
        self.name = "Kenyan"

    def speak_sheng(self):
        """ Defines how Kenyan says hello """
        return "Niaje?"


class British:
    """ British speaker """
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        """ Defines how British says hello """
        return "Hello"

class Adapter:
    """ Changes generic method name to individualized method names """
    def __init__(self, obj, **adapted_method):
        """ Changes the name of the method """
        self._object = obj

        # Add a new dictionary item that maps generic method name to concrete method
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """ Return the rest of the attributes """
        return getattr(self._object, attr)

# List to store speaker objects
OBJECTS = []

# Create Kenyan object
KEN = Kenyan()

# Create British object
GBR = British()

# Append objects to objects list
OBJECTS.append(Adapter(KEN, speak=KEN.speak_sheng))
OBJECTS.append(Adapter(GBR, speak=GBR.speak_english))

# Print greetings
for OBJ in OBJECTS:
    print("{} says {}".format(OBJ.name, OBJ.speak()))
