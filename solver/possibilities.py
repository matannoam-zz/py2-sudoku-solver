from .indices import Indices


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

    def groups_for(self, i, j):
        indicies_groups = [
            Indices.row_indices_without_space(i, j),
            Indices.column_indices_without_space(i, j),
            Indices.nonant_indices_without_space(i, j)]
        return [
            self.get_by_list(indices)
            for indices in indicies_groups]
