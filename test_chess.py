import sys
import unittest
from chess import *


class FastChessTests(unittest.TestCase):
    def test_one_piece_goes_anywhere(self):
        for i in range(1, 11):
            for j in range(1, 13):
                self.assertEqual(i * j, count_no_coverage_states(i, j, 1, 0, 0, 0, 0))
                self.assertEqual(i * j, count_no_coverage_states(i, j, 0, 1, 0, 0, 0))
                self.assertEqual(i * j, count_no_coverage_states(i, j, 0, 0, 1, 0, 0))
                self.assertEqual(i * j, count_no_coverage_states(i, j, 0, 0, 0, 1, 0))
                self.assertEqual(i * j, count_no_coverage_states(i, j, 0, 0, 0, 0, 1))

    def test_2_kings_on_tiny_board(self):
        self.assertEqual(0, count_no_coverage_states(2, 2, 2, 0, 0, 0, 0))

    def test_2_rooks_on_tiny_board(self):
        self.assertEqual(2, count_no_coverage_states(2, 2, 0, 0, 0, 2, 0))

    def test_2_knights_on_tiny_board(self):
        self.assertEqual(6, count_no_coverage_states(2, 2, 0, 0, 0, 0, 2))

    def test_3_knights_on_tiny_board(self):
        self.assertEqual(4, count_no_coverage_states(2, 2, 0, 0, 0, 0, 3))

    def test_2_bishops_on_tiny_board(self):
        self.assertEqual(4, count_no_coverage_states(2, 2, 0, 0, 2, 0, 0))

    def test_2_queens_on_tiny_board(self):
        self.assertEqual(0, count_no_coverage_states(2, 2, 0, 2, 0, 0, 0))

    def test_provided_2kings_1rook_3x3(self):
        self.assertEqual(4, count_no_coverage_states(3, 3, 2, 0, 0, 1, 0))

    def test_provided_2rooks_4knights_4x4(self):
        self.assertEqual(8, count_no_coverage_states(4, 4, 0, 0, 0, 2, 4))


class SlowChessTests(unittest.TestCase):
    def test_known_8queen_8x8(self):
        self.assertEqual(92, count_no_coverage_states(8, 8, 0, 8, 0, 0, 0))


class RequiredTest(unittest.TestCase):
    def test_required_example(self):
        self.assertEqual(20136752, count_no_coverage_states(6, 9, 2, 1, 1, 1, 1))


if __name__ == "__main__":
    fast = unittest.defaultTestLoader.loadTestsFromTestCase(FastChessTests)
    slow = unittest.defaultTestLoader.loadTestsFromTestCase(SlowChessTests)
    required = unittest.defaultTestLoader.loadTestsFromTestCase(RequiredTest)

    all_tests = unittest.TestSuite([fast, slow, required])
    suite = eval(sys.argv[1])
    unittest.TextTestRunner().run(suite)
