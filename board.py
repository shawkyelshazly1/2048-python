import random


class Board:
    def __init__(self):
        self.current_score = 0
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

    def get_board(self):
        for row in self.board:
            print(row)

    def shift(self, direction):
        if direction == 'left':
            self.shift_left()
            self.sum_left()
            self.shift_left()
        elif direction == 'right':
            self.shift_right()
            self.sum_right()
            self.shift_right()
        elif direction == 'up':
            self.shift_up()
            self.sum_up()
            self.shift_up()
        elif direction == 'down':
            self.shift_down()
            self.sum_down()
            self.shift_down()

    def reset_board(self):
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

    def new_game(self):
        pass

    def get_empty_locations(self):
        empty_locations = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.get_value_from_board(row, column) == 0:
                    empty_locations.append([row, column])

        return empty_locations

    def get_value_from_board(self, row, column):
        return self.board[row][column]

    def set_board_value(self, row, column, value):
        self.board[row][column] = value

    def spawn_random_tile(self):
        empty_locations = self.get_empty_locations()
        if len(empty_locations) > 0:
            location = random.choice(empty_locations)
            self.board[location[0]][location[1]] = 2

            return location

    def get_board_len(self):
        return len(self.board)

    def shift_left(self):
        for row in range(self.get_board_len()):
            temp_row = []
            for column in range(1, len(self.board[row])):
                if self.get_value_from_board(row, column) == 0:
                    pass
                else:
                    pointer = column-1
                    pointer2 = column
                    while pointer >= 0:
                        if self.get_value_from_board(row, pointer) == 0:
                            self.set_board_value(
                                row, pointer, self.get_value_from_board(row, pointer2))
                            self.set_board_value(row, pointer2, 0)
                            pointer -= 1
                            pointer2 -= 1

                        else:
                            break

    def shift_right(self):
        for row in range(self.get_board_len()):
            for column in range(len(self.board[row])-1, -1, -1):
                if not self.get_value_from_board(row, column) == 0:
                    pointer = column + 1
                    pointer2 = column
                    while pointer <= len(self.board[row])-1:
                        if self.get_value_from_board(row, pointer) == 0:
                            self.set_board_value(
                                row, pointer, self.get_value_from_board(row, pointer2))
                            self.set_board_value(row, pointer2, 0)
                            pointer += 1
                            pointer2 += 1
                        else:
                            break

    def shift_up(self):
        for column in range(self.get_board_len()):
            for row in range(1, len(self.board[column])):
                if not self.get_value_from_board(row, column) == 0:
                    pointer = row-1
                    pointer2 = row
                    while pointer >= 0:
                        if self.get_value_from_board(pointer, column) == 0:
                            self.set_board_value(
                                pointer, column, self.get_value_from_board(pointer2, column))
                            self.set_board_value(pointer2, column, 0)
                            pointer -= 1
                            pointer2 -= 1
                        else:
                            break

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

    def is_board_full(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.get_value_from_board(row, column) == 0:
                    return False

        return True

    def sum_left(self):
        for row in range(len(self.board)):
            column = 0
            while column < len(self.board[row])-1:
                pointer = column + 1
                if self.get_value_from_board(row, column) == self.get_value_from_board(row, pointer):
                    new_value = self.get_value_from_board(
                        row, column) + self.get_value_from_board(row, pointer)
                    self.set_board_value(row, column, new_value)
                    self.set_board_value(row, pointer, 0)
                    self.increase_Score(new_value)
                    column += 2
                else:
                    column += 1

    def sum_right(self):
        for row in range(len(self.board)):
            column = len(self.board[row])-1
            while column > 0:
                pointer = column-1
                if self.get_value_from_board(row, column) == self.get_value_from_board(row, pointer):
                    new_value = self.get_value_from_board(
                        row, column) + self.get_value_from_board(row, pointer)
                    self.set_board_value(row, column, new_value)
                    self.set_board_value(row, pointer, 0)
                    self.increase_Score(new_value)
                    column -= 2
                else:
                    column -= 1

    def sum_up(self):
        for column in range(self.get_board_len()):
            row = 0
            while row < self.get_board_len()-1:
                pointer = row + 1
                if self.get_value_from_board(row, column) == self.get_value_from_board(pointer, column):
                    new_value = self.get_value_from_board(
                        row, column) + self.get_value_from_board(pointer, column)
                    self.set_board_value(row, column, new_value)
                    self.set_board_value(pointer, column, 0)
                    self.increase_Score(new_value)
                    row += 2
                else:
                    row += 1

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
                    self.increase_Score(new_value)
                    row -= 2
                else:
                    row -= 1

    def increase_Score(self, value):
        self.current_score += value

    def get_current_score(self):
        return self.current_score

    def still_more_moves(self):
        for row in range(self.get_board_len()):
            for column in range(self.get_board_len()-1):
                if self.get_value_from_board(row, column) == self.get_value_from_board(row, column + 1):
                    return True

        for column in range(self.get_board_len()):
            for row in range(self.get_board_len()-1):
                if self.get_value_from_board(row, column) == self.get_value_from_board(row+1, column):
                    return True

        return False
