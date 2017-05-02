""" Demonstrates composite pattern """

class Component(object):
    """ Abstract class """

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        """ Defines function to be implemented by child classes """
        pass


class Child(Component):
    """ Concrete class that inherits from Component Class """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # Store the name of your child item here
        self.name = args[0]

    def component_function(self):
        """ Prints name of child item """
        print("{}".format(self.name))


class Composite(Component):
    """ Concrete class that maintains tree recursive structure """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # Store the name of the composite object here
        self.name = args[0]

        # Store child items here
        self.children = []

    def append_child(self, child):
        """ Adds new child items """
        self.children.append(child)

    def remove_child(self, child):
        """ Removes child items """
        self.children.remove(child)

    def component_function(self):
        """ Prints the name of the composite object and child items """
        print("{}".format(self.name))

        # Print children names
        for item in self.children:
            item.component_function()

# Build composite submenu 1
SUB1 = Composite("submenu1")

# Create new child submenus
SUB11 = Child("sub_submenu 11")
SUB12 = Child("sub_submenu 12")

# Add submenus created to submenu 1
SUB1.append_child(SUB11)
SUB1.append_child(SUB12)

# Build a top level composite menu
TOP = Composite("top_menu")

# Build a non-comopsite submenu 2
SUB2 = Child("submenu2")

# Add submenu 1 and 2 to top level menu
TOP.append_child(SUB1)
TOP.append_child(SUB2)

# Test pattern works
TOP.component_function()
