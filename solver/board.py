from copy import deepcopy

from .possibilities import Possibilities


class Board(object):

    def __init__(self, digit_array):
        self.digit_array = deepcopy(digit_array)
        self.possibilities = Possibilities(self)

    def get(self, i, j):
        return self.digit_array[i][j]

    def set(self, i, j, digit):
        self.digit_array[i][j] = digit
        self.possibilities.update()

    def to_native(self):
        return deepcopy(self.digit_array)

    def get_list(self, indices):
        return [self.get(*i) for i in indices]

    def get_possibilities(self, i, j):
        return self.possibilities.get(i, j)

    def related_possibilities_groups(self, i, j):
        return self.possibilities.related_groups(i, j)
