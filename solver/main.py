from copy import deepcopy

from .indices import Indices


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


class Possibilties(object):

    def __init__(self, board):
        self.board = board

    def get_by_list(self, indices):
        return [self.get(i[0], i[1]) for i in indices]

    def get(self, i, j):
        if self.board[i][j]:
            return [self.board[i][j]]

        row_indicies = Indices.row_indices_for_space(i, j)
        column_indicies = Indices.column_indices_for_space(i, j)
        nonant_indicies = Indices.nonant_indices_for_space(i, j)

        return list(self.missing_from_all(
            [row_indicies, column_indicies, nonant_indicies]))

    def missing_from_all(self, groups_of_indices):
        missing_from_groups = [
            self.missing(indices) for indices in groups_of_indices]
        return set.intersection(*missing_from_groups)

    def missing(self, indices):
        one_to_nine = range(1, 10)
        return set(
            digit for digit in one_to_nine
            if digit not in self.board_spaces(indices))

    def board_spaces(self, indices):
        return [self.board[i[0]][i[1]] for i in indices]
