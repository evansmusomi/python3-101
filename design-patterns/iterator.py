""" Demonstrates iterator pattern """


def count_to(count):
    """ Implements custom iterator """

    # List of numbers in Swahili
    numbers_in_swahili = ["moja", "mbili", "tatu", "nne", "tano"]

    # Create tuple with format (1, "moja") using built-in iterator
    iterator = zip(range(count), numbers_in_swahili)

    # Iterate through iterable list, extract Swahili numbers
    # Put them in a generator called number
    for position, number in iterator:
        # returns a 'generator' yielding numbers in Swahili
        yield number


# Test generator returned by our iterator
for num in count_to(4):
    print("{}".format(num))
