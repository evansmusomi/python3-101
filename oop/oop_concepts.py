class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, {}".format(self.name))

p1 = Person('Evans')
p1.say_hello()

p2 = Person('Musomi')
p2.say_hello()
