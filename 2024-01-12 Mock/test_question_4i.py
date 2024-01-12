'''
@author: Lilian
'''
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from question_4 import ColourPuzzle


class Question4iTest(unittest.TestCase):

    # @weight(7)
    @number("4.i.1")
    def testInit(self):
        """
        Question 4.i: Test that the init method makes a copy of the puzzle passed in parameter.
        """
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertListEqual(board, puzzle._board)
        self.assertNotEqual(id(board), id(puzzle._board))

    # @weight(8)
    @number("4.i.2")
    def testInitInvalidPuzzle(self):
        """
        Question 4.i: Test that a ValueError is raised when the puzzle is not a 4x4 board, or if the puzzle does not contain 5 tiles of each colour {1, 2, 3} and one empty space {0}.
        """
        board = [[2, 1, 2],
                 [2, 1, 3],
                 [3, 2, 3],
                 [1, 3, 1]]
        self.assertRaises(ValueError, ColourPuzzle, board)
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 0, 0]]
        self.assertRaises(ValueError, ColourPuzzle, board)
        board = [[2, 1, 2, 1],
                 [2, 1, 4, 2],
                 [1, 2, 4, 4],
                 [1, 4, 4, 0]]
        self.assertRaises(ValueError, ColourPuzzle, board)
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 1, 1]]
        self.assertRaises(ValueError, ColourPuzzle, board)


if __name__ == "__main__":
    unittest.main()
