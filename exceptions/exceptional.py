'''A module for demonstrating exceptions.'''
import sys


def convert(s):
    '''Converts to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1
