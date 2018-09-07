from .indices import Indices, Row, Column, Nonant


class Possibilities(object):

    def __init__(self, board):
        self.saved = [[None] * 9 for i in xrange(9)]
        self.updater = Updater(board)
        self.update()

    def update(self):
        for i, j in Indices.all():
            self.saved[i][j] = self.updater.get(i, j)

    def get(self, i, j):
        return self.saved[i][j]

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


class Updater(object):

    def __init__(self, board):
        self.board = board

    def get(self, *index):
        if self.board.get(*index):
            return [self.board.get(*index)]

        indicies_groups = [
            Row.for_space(*index),
            Column.for_space(*index),
            Nonant.for_space(*index)]

        return list(self.missing_from_all(indicies_groups))

    def missing_from_all(self, groups_of_indices):
        missing_from_groups = [
            self.missing(indices) for indices in groups_of_indices]
        return set.intersection(*missing_from_groups)

    def missing(self, indices):
        one_to_nine = range(1, 10)
        return set(
            digit for digit in one_to_nine
            if digit not in self.board.get_list(indices))
