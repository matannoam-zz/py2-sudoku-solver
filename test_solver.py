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

    def test_returns_input_for_solved_puzzle(self):
        initial_board = deepcopy(self.solution)
        solver = Solver(initial_board)
        self.assertEqual(solver.solve(), self.solution)

    def test_missing_single_digits_from_rows(self):
        initial_board = deepcopy(self.solution)
        for row in initial_board:
            row[0] = None
        solver = Solver(initial_board)
        self.assertEqual(solver.solve(), self.solution)

    def test_missing_single_digits_from_columns(self):
        initial_board = deepcopy(self.solution)
        initial_board[0] = [None] * 9
        solver = Solver(initial_board)
        self.assertEqual(solver.solve(), self.solution)
