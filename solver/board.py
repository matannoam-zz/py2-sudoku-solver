from copy import deepcopy


class Board(object):

    def __init__(self, digit_array):
        self.digit_array = deepcopy(digit_array)

    def get(self, i, j):
        return self.digit_array[i][j]

    def set(self, i, j, digit):
        self.digit_array[i][j] = digit

    def to_native(self):
        return deepcopy(self.digit_array)

    def get_list(self, indices):
        return [self.get(*i) for i in indices]
