from .indices import Row, Column, Nonant


class PossibleFinder(object):

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
