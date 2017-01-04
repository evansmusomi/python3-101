'''A module for demonstrating exceptions.'''


def convert(s):
    '''Converts to an integer.'''
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        print("Conversion failed!")
    return x
