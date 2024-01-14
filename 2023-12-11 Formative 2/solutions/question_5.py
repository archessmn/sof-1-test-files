class Blotris:
    _rows: int = 0
    _columns: int = 0
    _board: list[list[int]] = []

    def __init__(self, rows: int, columns: int) -> None:
        """Initialises the board with the given number of
        rows and columns

        Args:
            rows (int): Number of rows to create
            columns (int): Number of columns to create

        Raises:
            ValueError: Raised if the number of rows or
            columns are less than 5
        """
        # Raise ValueError if the rows or columns are less than 5
        if rows < 5 or columns < 5:
            raise ValueError("Rows and columns must be longer than 5")

        # Set the board to empty
        self._board = []

        # Set each value in row and column to 0
        for row_num in range(rows):
            self._board.append([])
            for col_num in range(columns):
                self._board[-1].append(0)

        # Set class attributes
        self._rows = rows
        self._columns = columns

    def add(self, shape: list[list[int]], row: int, col: int) -> bool:
        """Adds a shape to the board, provided in a 2d list and returns
        a boolean depending on the result

        Args:
            shape (list[list[int]]): A 2d list defining the shape to be
            added to the board
            row (int): The row to place the top left corner of the
            shape in
            col (int): The column to place the top left corner of the
            shape in

        Returns:
            bool: True if the shape has been added, False if the shape
            was out of bounds or overlapped with existing rows
        """

        # Return False if out of bounds
        if (row + len(shape) > self._rows
                or col + len(shape[0]) > self._columns
                or row < 0 or col < 0):
            return False

        # Search for an overlap
        for shape_row in range(row, row + len(shape)):
            for shape_col in range(col, col + len(shape[0])):
                if (shape[shape_row - row][shape_col - col] != 0
                        and self._board[shape_row][shape_col] != 0):
                    # Return false if the shape overlaps
                    return False

        # If no overlap, change the board
        for shape_row in range(row, row + len(shape)):
            for shape_col in range(col, col + len(shape[0])):
                # If the current box in the shape is a 1
                if shape[shape_row - row][shape_col - col] == 1:
                    # Set the value in the board
                    self._board[shape_row][shape_col] = 1

        # Return True after adding the shape
        return True

    def update(self) -> None:
        """Removes full rows and shifts down the rest of the board,
        doesn't return anything
        """
        # For each row in the board, remove it if it doesn't contain
        # a 0 and insert a new empty row at the top of the board
        for row_num in range(len(self._board)):
            if 0 not in self._board[row_num]:
                self._board.pop(row_num)
                self._board.insert(0, [0] * self._columns)
