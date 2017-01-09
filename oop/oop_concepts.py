class Classroom:

    def __init__(self):
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for person in self._people:
            person.say_hello()

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, {}".format(self.name))

room = Classroom()
room.add_person(Person("Evans"))
room.add_person(Person("Musomi"))
room.add_person(Person("Muema"))
