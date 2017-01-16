from collections import Counter


class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        # check for duplicate numbers
        c = Counter(self.entries.values())
        occurrences = [k for k, v in self.entries.items() if c[v] > 1]
        if len(occurrences) > 0:
            return False

        return True

    def get_names(self):
        return list(self.entries.keys())

    def get_numbers(self):
        return list(self.entries.values())
