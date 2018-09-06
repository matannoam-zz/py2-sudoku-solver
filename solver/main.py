from .board import Board


class Solver(object):

    def __init__(self, board_array):
        self.board = Board(board_array)

    def solve(self):
        changed = True
        while changed:
            changed = self.changes_one_board_pass()

        return self.board.to_native()

    def changes_one_board_pass(self):
        return any(
            self.sets_space(i, j)
            for i in xrange(9)
            for j in xrange(9))

    def sets_space(self, i, j):
        if self.board.get(i, j) is None:
            digit = (
                Steps.only_digit_possible(self.board, i, j) or
                Steps.digit_needed(self.board, i, j))
            if digit:
                self.board.set(i, j, digit)
                return True
        return False


class Steps(object):

    @classmethod
    def only_digit_possible(cls, board, i, j):
        digits_possible = board.get_possibilities(i, j)
        if len(digits_possible) == 1:
            return digits_possible[0]
        return None

    @classmethod
    def digit_needed(cls, board, i, j):
        possibilities_groups = board.related_possibilities_groups(i, j)
        for digit in board.get_possibilities(i, j):
            needed = Utilities.missing_from_any(digit, possibilities_groups)
            if needed:
                return digit
        return None


class Utilities(object):
    @classmethod
    def in_any(cls, item, items_groups):
        return any(item in items for items in items_groups)

    @classmethod
    def missing_from(cls, item, items_groups):
        return not cls.in_any(item, items_groups)

    @classmethod
    def missing_from_any(cls, item, groups_of_groups):
        return any(
            cls.missing_from(item, items_groups)
            for items_groups in groups_of_groups)
