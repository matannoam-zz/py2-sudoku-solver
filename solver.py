class Solver(object):

    def __init__(self, board):
        self.board = board

    def solve(self):
        for i in xrange(9):
            for j in xrange(9):
                row = self.board[i]
                missing_from_row = self.missing(row)
                column = [board_row[j] for board_row in self.board]
                missing_from_column = self.missing(column)
                missing_from_both = [
                    digit for digit in missing_from_row
                    if digit in missing_from_column]

                if len(missing_from_both) == 1:
                    self.board[i][j] = missing_from_both[0]

        return self.board

    def missing(self, portion):
        one_to_nine = range(1, 10)
        return [
            digit for digit in one_to_nine
            if digit not in portion]
