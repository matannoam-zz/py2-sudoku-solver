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

    def test_needs_multiple_passes(self):
        initial_board = deepcopy(self.solution)
        for i in [0, 4, 8]:
            for j in [0, 4, 8]:
                initial_board[i][j] = None

        initial_board[2][2] = initial_board[6][6] = None

        self.assert_finds_solution(initial_board)

    def test_requires_digit(self):
        initial_board = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, 1, None, None, None, None, None],
            [None, None, None, None, None, None, 1, None, None],
            [None, None, 1, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, 1, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]]

        solver = Solver(initial_board)
        partial_solution = deepcopy(initial_board)
        partial_solution[0][0] = 1
        self.assertEqual(solver.solve(), partial_solution)

    def test_avoids_conflict_with_two_spaces(self):
        initial_board = [
            [3, None, None, None, None, None, None, None, None],
            [4, 5, 6, 3, None, None, None, None, None],
            [7, 8, 9, 5, None, None, None, None, None],
            [None, None, None, 6, None, None, None, None, None],
            [None, None, None, 7, None, None, None, None, None],
            [None, None, None, 8, None, None, None, None, None],
            [None, None, None, 9, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]]

        solver = Solver(initial_board)
        partial_solution = deepcopy(initial_board)
        partial_solution[0][3] = 4
        self.assertEqual(solver.solve(), partial_solution)
