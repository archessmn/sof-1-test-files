'''
@author: Lilian
'''
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from question_4 import ColourPuzzle


class Question4iiiTest(unittest.TestCase):

    # @weight(5)
    @number("4.iii.1")
    def testMoves(self):
        """
        Question 4.iii: Test that the move method returns true for valid moves, and the board is modified accordingly.
        """
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 0, 3],
                 [1, 3, 1, 3]]
        puzzle = ColourPuzzle(board)
        self.assertTrue(puzzle.moveLeftTile())
        resultingBoard = [[2, 1, 2, 1],
                          [2, 1, 3, 2],
                          [3, 0, 2, 3],
                          [1, 3, 1, 3]]
        self.assertListEqual(resultingBoard, puzzle._board)
        self.assertTrue(puzzle.moveLowerTile())
        resultingBoard = [[2, 1, 2, 1],
                          [2, 1, 3, 2],
                          [3, 3, 2, 3],
                          [1, 0, 1, 3]]
        self.assertListEqual(resultingBoard, puzzle._board)
        self.assertTrue(puzzle.moveRightTile())
        resultingBoard = [[2, 1, 2, 1],
                          [2, 1, 3, 2],
                          [3, 3, 2, 3],
                          [1, 1, 0, 3]]
        self.assertListEqual(resultingBoard, puzzle._board)
        self.assertTrue(puzzle.moveUpperTile())
        resultingBoard = [[2, 1, 2, 1],
                          [2, 1, 3, 2],
                          [3, 3, 0, 3],
                          [1, 1, 2, 3]]
        self.assertListEqual(resultingBoard, puzzle._board)

    # @weight(5)

    @number("4.iii.2")
    def testInvalidMoves(self):
        """
        Question 4.iii: Test that the method returns false for invalid move and that the board remains unchanged.
        """
        board = [[2, 1, 2, 1],
                 [2, 1, 3, 2],
                 [3, 2, 3, 3],
                 [1, 3, 1, 0]]
        puzzle = ColourPuzzle(board)
        self.assertFalse(puzzle.moveRightTile())
        self.assertListEqual(board, puzzle._board)
        self.assertFalse(puzzle.moveLowerTile())
        self.assertListEqual(board, puzzle._board)
        board = [[0, 1, 2, 1],
                 [1, 2, 3, 2],
                 [3, 3, 2, 3],
                 [1, 3, 1, 2]]
        puzzle = ColourPuzzle(board)
        self.assertFalse(puzzle.moveLeftTile())
        self.assertListEqual(board, puzzle._board)
        self.assertFalse(puzzle.moveUpperTile())
        self.assertListEqual(board, puzzle._board)


if __name__ == "__main__":
    unittest.main()
