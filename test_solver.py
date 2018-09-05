from unittest import TestCase

from copy import deepcopy

from solver import Solver


class SolverTests(TestCase):

    def setUp(self):
        self.solution = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5]]

    def assert_finds_solution(self, initial_board):
        solver = Solver(initial_board)
        self.assertEqual(solver.solve(), self.solution)

    def test_returns_input_for_solved_puzzle(self):
        initial_board = deepcopy(self.solution)
        self.assert_finds_solution(initial_board)

    def test_missing_single_digits_from_rows(self):
        initial_board = deepcopy(self.solution)
        for row in initial_board:
            row[0] = None

        self.assert_finds_solution(initial_board)

    def test_missing_single_digits_from_columns(self):
        initial_board = deepcopy(self.solution)
        initial_board[0] = [None] * 9

        self.assert_finds_solution(initial_board)

    def test_missing_two_digits_each_row_and_column(self):
        initial_board = deepcopy(self.solution)
        initial_board[0][0] = initial_board[0][1] = None
        initial_board[1][0] = initial_board[1][1] = None

        self.assert_finds_solution(initial_board)

    def test_missing_single_digits_from_nonants(self):
        initial_board = deepcopy(self.solution)
        for i in [0, 4, 8]:
            for j in [0, 4, 8]:
                initial_board[i][j] = None

        self.assert_finds_solution(initial_board)
