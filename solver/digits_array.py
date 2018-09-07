from .indices import Row, Column, Nonant


class DigitsArray(object):

    def __init__(self):
        self.native = [[None] * 9 for i in xrange(9)]

    def get(self, i, j):
        return self.native[i][j]

    def set(self, i, j, digits):
        self.native[i][j] = digits

    def get_list(self, indices):
        return [self.get(*i) for i in indices]

    def related_groups(self, *index):
        indicies_groups = [
            Row.without_space(*index),
            Column.without_space(*index),
            Nonant.without_space(*index)]
        return [
            self.get_list(indices)
            for indices in indicies_groups]
