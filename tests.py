

import collections
from hashlib import new


class Board_Test:
    def __init__(self):
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

    def get_board_len(self):
        return len(self.board)

    def get_value_from_board(self, row, column):
        return self.board[row][column]

    def set_board_value(self, row, column, value):
        self.board[row][column] = value

    def sum_down(self):
        for column in range(self.get_board_len()):
            row = self.get_board_len()-1
            while row > 0:
                pointer = row - 1
                if self.get_value_from_board(row, column) == self.get_value_from_board(pointer, column):
                    new_value = self.get_value_from_board(
                        row, column) + self.get_value_from_board(pointer, column)
                    self.set_board_value(row, column, new_value)
                    self.set_board_value(pointer, column, 0)
                    row -= 2
                else:
                    row -= 1

    def shift_down(self):
        for column in range(self.get_board_len()):
            for row in range(len(self.board[column])-1, -1, -1):
                if not self.get_value_from_board(row, column) == 0:
                    pointer = row + 1
                    pointer2 = row
                    while pointer <= len(self.board[column])-1:
                        if self.get_value_from_board(pointer, column) == 0:
                            self.set_board_value(
                                pointer, column, self.get_value_from_board(pointer2, column))
                            self.set_board_value(pointer2, column, 0)
                            pointer += 1
                            pointer2 += 1
                        else:
                            break


board = Board_Test()

board.board = [[0, 2, 4, 2],
               [2, 2, 2, 2],
               [0, 2, 2, 0],
               [2, 2, 4, 2]]

board.shift_down()
board.sum_down()
board.shift_down()

if board.board == [[0, 0, 0, 0],
                   [0, 0, 4, 0],
                   [0, 4, 4, 2],
                   [4, 4, 4, 4]]:
    print('success')
else:
    print('failed\n')
    for row in board.board:
        print(row)
