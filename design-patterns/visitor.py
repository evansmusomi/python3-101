""" Demonstrates visitor pattern """


class House(object):
    """ Represents house - class being visited """

    def accept(self, visitor):
        """ Interface to accept visitors. Triggers the visit operation """
        visitor.visit(self)

    def work_on_plumbing(self, plumber):
        """ Allows plumber to do work in the house """
        print(self, "worked on by", plumber)

    def work_on_electricity(self, electrician):
        """ Allows electrician to do work in the house """
        print(self, "worked on by", electrician)

    def __str__(self):
        """ Returns class name when House object is printed """
        return self.__class__.__name__


class Visitor(object):
    """ Abstract visitor """

    def __str__(self):
        """ Returns class name when visitor object is printed """
        return self.__class__.__name__


class Plumber(Visitor):
    """ Concrete visitor: Plumber """

    def visit(self, house):
        """ Gives visitor reference to object to visit (House) """
        house.work_on_plumbing(self)


class Electrician(Visitor):
    """ Concrete visitor: Electrician """

    def visit(self, house):
        """ Gives visitor reference to object to visit (House) """
        house.work_on_electricity(self)


# Create a plumber
plumber = Plumber()

# Create an electrician
electrician = Electrician()

# Create a house
home = House()

# Let the house accept the plumber and work on the house by invoking visit()
home.accept(plumber)

# Let the house accept the electrician and work on the house by invoking
# visit()
home.accept(electrician)
