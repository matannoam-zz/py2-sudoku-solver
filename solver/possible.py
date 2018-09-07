from .indices import Row, Column, Nonant, Indices


class MissingFinder(object):

    def __init__(self, board):
        self.board = board

    def update(self):
        for index in Indices.all():
            digits = self.get(*index)
            self.board.possible.set(index[0], index[1], digits)

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


class ExclusionFinder(object):

    def __init__(self, possible):
        self.possible = possible

    def update(self):
        one_to_nine = range(1, 10)
        for nonant in xrange(9):
            for digit in one_to_nine:
                indices = [
                    index for index in Nonant.indices(nonant)
                    if digit in self.possible.get(*index)]
                if len(indices) > 1:
                    self.remove_possible_row(indices, digit)
                    self.remove_possible_column(indices, digit)

    def remove_possible_row(self, indices, digit):
        if Row.same(indices):
            for index in Row.for_space(*indices[0]):
                if index not in indices:
                    self.remove_possible(index[0], index[1], digit)

    def remove_possible_column(self, indices, digit):
        if Column.same(indices):
            for index in Column.for_space(*indices[0]):
                if index not in indices:
                    self.remove_possible(index[0], index[1], digit)

    def remove_possible(self, i, j, digit):
        possible = self.possible.get(i, j)
        if digit in possible:
            possible.remove(digit)
        self.possible.set(i, j, possible)
