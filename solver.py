from copy import deepcopy


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
            if (self.sets_board_if_only_one_possible(i, j) or
                    self.sets_board_if_digit_needed(i, j)):
                return True
        return False

    def sets_board_if_only_one_possible(self, i, j):
        possibilities = self.possibilities.get(i, j)
        if len(possibilities) == 1:
            self.board[i][j] = possibilities[0]
            return True
        else:
            return False

    def sets_board_if_digit_needed(self, i, j):
        row_possibilities = self.possibilities.get_by_list(
            Indices.row_indices_without_space(i, j))
        column_possibilities = self.possibilities.get_by_list(
            Indices.column_indices_without_space(i, j))
        nonant_possiblities = self.possibilities.get_by_list(
            Indices.nonant_indices_without_space(i, j))

        for digit in self.possibilities.get(i, j):
            possibilities_groups = [
                row_possibilities,
                column_possibilities,
                nonant_possiblities]
            if not Utilities.in_any_for_all(digit, possibilities_groups):
                self.board[i][j] = digit
                return True
        return False


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


class Indices(object):

    @classmethod
    def row_indices_for_space(cls, i, j):
        return [(i, k) for k in xrange(9)]

    @classmethod
    def column_indices_for_space(self, i, j):
        return [(k, j) for k in xrange(9)]

    @classmethod
    def nonant_indices_for_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)]

    @classmethod
    def row_indices_without_space(cls, i, j):
        return [(i, k) for k in xrange(9) if k != j]

    @classmethod
    def column_indices_without_space(self, i, j):
        return [(k, j) for k in xrange(9) if k != i]

    @classmethod
    def nonant_indices_without_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)
            if x != i or y != j]
