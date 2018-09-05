from copy import deepcopy


class Solver(object):

    def __init__(self, board):
        self.board = deepcopy(board)

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
            if self.sets_board_if_only_one_possible(i, j):
                return True
        return False

    def get_possibilities(self, i, j):
        missing_from_row = self.missing(self.row_indices_for_space(i, j))
        missing_from_column = self.missing(self.column_indices_for_space(i, j))
        missing_from_nonant = self.missing(self.nonant_indices_for_space(i, j))

        return [
            digit for digit in missing_from_row
            if digit in missing_from_column and
            digit in missing_from_nonant]

    def sets_board_if_only_one_possible(self, i, j):
        possibilities = self.get_possibilities(i, j)
        if len(possibilities) == 1:
            self.board[i][j] = possibilities[0]
            return True
        else:
            return False

    def row_indices_for_space(self, i, j):
        return [(i, k) for k in xrange(9)]

    def column_indices_for_space(self, i, j):
        return [(k, j) for k in xrange(9)]

    def nonant_indices_for_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)]

    def missing(self, indices):
        one_to_nine = range(1, 10)
        return [
            digit for digit in one_to_nine
            if digit not in self.board_spaces(indices)]

    def board_spaces(self, indices):
        return [self.board[i[0]][i[1]] for i in indices]
