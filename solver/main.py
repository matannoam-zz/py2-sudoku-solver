from copy import deepcopy

from .indices import Indices
from .possibilities import Possibilties


class Solver(object):

    def __init__(self, board):
        self.board = deepcopy(board)
        self.possibilities = Possibilties(self.board)

    def solve(self):
        changed = True
        while changed:
            changed = self.changes_one_board_pass()

        return self.board

    def changes_one_board_pass(self):
        return any(
            self.sets_space(i, j)
            for i in xrange(9)
            for j in xrange(9))

    def sets_space(self, i, j):
        if self.board[i][j] is None:
            digit = (
                self.only_digit_possible(i, j) or
                self.digit_needed(i, j))
            if digit:
                self.board[i][j] = digit
                return True
        return False

    def only_digit_possible(self, i, j):
        possibilities = self.possibilities.get(i, j)
        if len(possibilities) == 1:
            return possibilities[0]
        return None

    def digit_needed(self, i, j):
        possibilities_groups = self.possibilties_groups_for(i, j)
        for digit in self.possibilities.get(i, j):
            if not Utilities.in_any_for_all(digit, possibilities_groups):
                return digit
        return None

    def possibilties_groups_for(self, i, j):
        indicies_groups = [
            Indices.row_indices_without_space(i, j),
            Indices.column_indices_without_space(i, j),
            Indices.nonant_indices_without_space(i, j)]
        return [
            self.possibilities.get_by_list(indices)
            for indices in indicies_groups]


class Utilities(object):
    @classmethod
    def in_any(cls, item, items_groups):
        return any(item in items for items in items_groups)

    @classmethod
    def in_any_for_all(cls, item, groups_of_groups):
        return all(
            cls.in_any(item, items_groups)
            for items_groups in groups_of_groups)
