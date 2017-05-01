""" Demonstrates singleton pattern """
class Borg:
    """The Borg class making class attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    """The singleton class that shares all its attributes among its various instances"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


# Create singleton object and add acronym
X = Singleton(SMS='Short Message Service')
print(X)
# Create another singleton object and see if same dictionary is referenced
Y = Singleton(MMS='Multimedia Messaging Service')
print(Y)
