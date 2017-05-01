""" Abstract factory example"""

class Dog:
    """ One of the objects """

    def speak(self):
        """ Implements dog's speech """
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """ Concrete factory """

    def get_pet(self):
        """returns a dog object"""
        return Dog()

    def get_food(self):
        """returns a dog food object"""
        return "Dog food!"

class PetStore:
    """ Houses abstract factory """

    def __init__(self, pet_factory=None):
        """ pet_factory is our abstract factory """
        self._pet_factory = pet_factory

    def show_pet(self):
        """shows a pet's info"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says hello by {}".format(pet.speak()))
        print("It eats {}".format(pet_food))


# Create concrete factory
FACTORY = DogFactory()
# Create pet store to house our abstract factory
SHOP = PetStore(FACTORY)
# Invoke utility method to show pet details
SHOP.show_pet()
