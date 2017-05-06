""" Demonstrates the strategy pattern """

# import types module
import types


class Strategy(object):
    """ The strategy pattern class """

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # if a reference to a function is provided replace execute method with
        # the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        """ The default method. Prints name of strategy being used. """
        print("{} is used!".format(self.name))


def strategy_one(self):
    """ Replacement strategy 1 """
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self):
    """ Replacement strategy 2 """
    print("{} is used to execute method 2".format(self.name))


# Create default strategy and execute
s0 = Strategy()
s0.execute()

# Create first variation of default strategy by providing a new behaviour
s1 = Strategy(strategy_one)
s1.name = "Strategy 1"
s1.execute()

# Create second variation of default strategy by providing a new behaviour
s2 = Strategy(strategy_two)
s2.name = "Strategy 2"
s2.execute()
