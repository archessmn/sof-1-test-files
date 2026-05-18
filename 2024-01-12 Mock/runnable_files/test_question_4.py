from test_class import TestCase, number

from question_4 import ColourPuzzle


class Question4iTest(TestCase):

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


class Question4iiTest(TestCase):

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


class Question4iiiTest(TestCase):

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


class Question4ivTest(TestCase):

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
