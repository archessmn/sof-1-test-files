'''
@author: Lilian
'''
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from question_4 import ColourPuzzle


class Question4iiTest(unittest.TestCase):

    # @weight(3)
    @number("4.ii.1")
    def testMatchPattern(self):
        """
        Question 4.ii: Test that matchPattern method returns true when the centre of the puzzle matches the given pattern.
        """
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertTrue(puzzle.matchPattern([[1, 3], [2, 3]]))
        board = [[2, 1, 2, 1],
                 [1, 2, 3, 2],
                 [3, 3, 2, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertTrue(puzzle.matchPattern([[2, 3], [3, 2]]))

    # @weight(2)
    @number("4.ii.2")
    def testPatternDontMatch(self):
        """
        Question 4.ii: Test that matchPattern method returns false when the centre of the puzzle does not match the given pattern.
        """
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertFalse(puzzle.matchPattern([[3, 1], [2, 3]]))
        board = [[2, 1, 2, 1],
                 [1, 2, 3, 2],
                 [3, 3, 2, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertFalse(puzzle.matchPattern([[2, 3], [2, 3]]))


if __name__ == "__main__":
    unittest.main()
