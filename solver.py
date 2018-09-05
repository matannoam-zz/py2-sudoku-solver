class Solver(object):

    def __init__(self, board):
        self.board = board

    def solve(self):
        for i, row in enumerate(self.board):
            missing_from_row = self.missing(row)
            if len(missing_from_row) == 1:
                self.board[i] = [
                    digit if digit else missing_from_row[0]
                    for digit in row]

        for j in xrange(9):
            column = [row[j] for row in self.board]
            missing_from_column = self.missing(column)
            if len(missing_from_column) == 1:
                self.board[column.index(None)][j] = missing_from_column[0]

        return self.board

    def missing(self, portion):
        one_to_nine = range(1, 10)
        return [
            digit for digit in one_to_nine
            if digit not in portion]
