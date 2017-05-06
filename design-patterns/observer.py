""" Demonstrates observer pattern """


class Subject(object):
    """ Represents what is being observed"""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """ Adds observer to list if not already there """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """ Removes observer """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        """ Notifies all observers unaware of change to subject """
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)


class Core(Subject):
    """ Represents nuclear reactor core """

    def __init__(self, name):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        """ Gets core temperature """
        return self._temp

    @temp.setter
    def temp(self, temp):
        """ Setter that sets core temperature """
        self._temp = temp
        # notify observers when someone updates core temperature
        self.notify()


class TempViewer:
    """ Observer blue print """

    def update(self, subject):
        """ Alert method that is invoked when notify() method in a concrete
        subject is invoked """
        print("Temperature Viewer: {} has Temperature {}".format(
            subject._name, subject._temp))


# Create subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Create observers
v1 = TempViewer()
v2 = TempViewer()

# Attach observers to our first core
c1.attach(v1)
c1.attach(v2)

# Change Core 1 temperature
c1.temp = 80
c1.temp = 90
