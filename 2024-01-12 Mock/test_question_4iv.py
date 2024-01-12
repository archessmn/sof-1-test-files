'''
@author: Lilian
'''
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from question_4 import ColourPuzzle


class Question4ivTest(unittest.TestCase):

    # @weight(10)
    @number("4.iv")
    def testSolvable(self):
        """
        Question 4.iv: Test that the method solvable returns the right output for several puzzles and several patterns.
        """
        board = [[1, 0, 1, 1],
                 [1, 2, 2, 2],
                 [2, 2, 3, 3],
                 [3, 3, 3, 1]]
        puzzle = ColourPuzzle(board)
        self.assertTrue(puzzle.solvable([[2, 2], [2, 3]], 0))
        self.assertTrue(puzzle.solvable([[2, 2], [2, 3]], 1))

        self.assertTrue(puzzle.solvable([[1, 2], [2, 3]], 2))
        self.assertTrue(puzzle.solvable([[1, 2], [2, 3]], 5))
        self.assertFalse(puzzle.solvable([[1, 2], [2, 3]], 1))
        self.assertFalse(puzzle.solvable([[1, 2], [2, 3]], 0))

        board = [[1, 1, 1, 1],
                 [1, 2, 2, 2],
                 [2, 2, 3, 3],
                 [3, 3, 3, 0]]
        puzzle = ColourPuzzle(board)
        self.assertTrue(puzzle.solvable([[2, 2], [3, 2]], 4))
        self.assertTrue(puzzle.solvable([[2, 2], [3, 2]], 5))
        self.assertFalse(puzzle.solvable([[2, 2], [3, 2]], 3))
        self.assertFalse(puzzle.solvable([[2, 2], [3, 2]], 0))


if __name__ == "__main__":
    unittest.main()
