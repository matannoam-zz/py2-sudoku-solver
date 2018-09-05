class Solver(object):

    def __init__(self, board):
        self.board = board

    def solve(self):
        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j] is None:
                    self.solve_space(i, j)

        return self.board

    def solve_space(self, i, j):
        missing_from_row = self.missing(self.row_for_space(i, j))
        missing_from_column = self.missing(self.column_for_space(i, j))
        missing_from_nonant = self.missing(self.nonant_for_space(i, j))

        missing_from_all = [
            digit for digit in missing_from_row
            if digit in missing_from_column and
            digit in missing_from_nonant]

        if len(missing_from_all) == 1:
            self.board[i][j] = missing_from_all[0]

    def row_for_space(self, i, j):
        return self.board[i]

    def column_for_space(self, i, j):
        return [board_row[j] for board_row in self.board]

    def nonant_for_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        nonant = []
        for x in xrange(nonant_x, nonant_x + 3):
            for y in xrange(nonant_y, nonant_y + 3):
                nonant.append(self.board[x][y])

        return nonant

    def missing(self, portion):
        one_to_nine = range(1, 10)
        return [
            digit for digit in one_to_nine
            if digit not in portion]
