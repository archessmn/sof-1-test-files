import copy


class ColourPuzzle:

    _board: list[list[int]]

    def __init__(self, puzzle: list[list[int]]):
        self._board = (copy.copy(puzzle) if sum(map(lambda row: row.count(0), puzzle)) == 1 and sum(map(lambda row: row.count(1), puzzle)) == 5 and sum(map(lambda row: row.count(2), puzzle)) == 5 and sum(map(
            lambda row: row.count(3), puzzle)) == 5 else exec("raise ValueError('Wrong number of colours')")) if len(puzzle) == 4 and all(len(row) == 4 for row in puzzle) else exec("raise ValueError('Puzzle is the wrong size')")

    def matchPattern(self, pattern: list[list[int]]):
        return all(map(lambda row_num: all(map(lambda column_num: pattern[row_num][column_num] == self._board[row_num + 1][column_num + 1], range(len(pattern[row_num])))), range(len(pattern))))

    def _findEmptySpace(self) -> tuple[int, int]:
        return list(filter(lambda i: i if i != None else False, list(map(lambda i: tuple([i, self._board[i].index(0)]) if 0 in self._board[i] else False, range(len(self._board))))))[0]

    def moveLowerTile(self) -> bool:
        return (lambda empty_coords: False if empty_coords[0] == 3 else bool((lambda: (self._board[empty_coords[0]].insert(empty_coords[1], self._board[empty_coords[0] + 1][empty_coords[1]]), self._board[empty_coords[0]].pop(empty_coords[1] + 1), self._board[empty_coords[0] + 1].insert(empty_coords[1], 0), self._board[empty_coords[0] + 1].pop(empty_coords[1] + 1)))()))(self._findEmptySpace())

    def moveLeftTile(self) -> bool:
        return (lambda empty_coords: False if empty_coords[1] == 0 else bool((lambda: (self._board[empty_coords[0]].insert(empty_coords[1], self._board[empty_coords[0]][empty_coords[1] - 1]), self._board[empty_coords[0]].pop(empty_coords[1] + 1), self._board[empty_coords[0]].insert(empty_coords[1] - 1, 0), self._board[empty_coords[0]].pop(empty_coords[1])))()))(self._findEmptySpace())

    def moveUpperTile(self) -> bool:
        return (lambda empty_coords: False if empty_coords[0] == 0 else bool((lambda: (self._board[empty_coords[0]].insert(empty_coords[1], self._board[empty_coords[0] - 1][empty_coords[1]]), self._board[empty_coords[0]].pop(empty_coords[1] + 1), self._board[empty_coords[0] - 1].insert(empty_coords[1], 0), self._board[empty_coords[0] - 1].pop(empty_coords[1] + 1)))()))(self._findEmptySpace())

    def moveRightTile(self) -> bool:
        return (lambda empty_coords: False if empty_coords[1] == 3 else bool((lambda: (self._board[empty_coords[0]].insert(empty_coords[1], self._board[empty_coords[0]][empty_coords[1] + 1]), self._board[empty_coords[0]].pop(empty_coords[1] + 1), self._board[empty_coords[0]].insert(empty_coords[1] + 1, 0), self._board[empty_coords[0]].pop(empty_coords[1] + 2)))()))(self._findEmptySpace())

    def solvable(self, pattern: list[list[int]], n) -> bool:
        return self.matchPattern(pattern) if n == 0 else (True if self.matchPattern(pattern) else any((lambda: ((self.moveUpperTile() if self.solvable(pattern, n-1) else not self.moveUpperTile()) if self.moveLowerTile() else False, (self.moveRightTile() if self.solvable(pattern, n-1) else not self.moveRightTile()) if self.moveLeftTile() else False, (self.moveLowerTile() if self.solvable(pattern, n-1) else not self.moveLowerTile()) if self.moveUpperTile() else False, (self.moveLeftTile() if self.solvable(pattern, n-1) else not self.moveLeftTile()) if self.moveRightTile() else False))()))
