from copy import deepcopy

from .possible import PossibleFinder
from .digits_array import DigitsArray
from .indices import Indices


class Board(object):

    def __init__(self, initial_digits):
        self.answers = deepcopy(initial_digits)
        self.possible = DigitsArray()
        self.possible_finder = PossibleFinder(self)
        self.update_possibilities()

    def get(self, i, j):
        return self.answers[i][j]

    def set(self, i, j, digit):
        self.answers[i][j] = digit
        self.update_possibilities()

    def update_possibilities(self):
        for i, j in Indices.all():
            digits = self.possible_finder.get(i, j)
            self.possible.set(i, j, digits)

    def to_native(self):
        return deepcopy(self.answers)

    def get_list(self, indices):
        return [self.get(*i) for i in indices]

    def get_possible(self, i, j):
        return self.possible.get(i, j)

    def related_possible_groups(self, i, j):
        return self.possible.related_groups(i, j)
