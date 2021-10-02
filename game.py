from square import Square
from board import Board
import pygame
import sys
import shelve

COLORS = {
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 210, 176),
    1024: (237, 197, 63),
    2048: (237, 194, 46)

}


class Game:
    def __init__(self, surface):
        self.current_score = 0
        self.highest_score = self.get_high_score()
        self.surface = surface
        self.board = Board()
        self.start_state = True
        self.tiles = []
        self.game_window = 'menu_window'

    def run(self):

        if self.start_state:
            self.start_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.key_movements(event)
                self.draw_tiles()

        self.draw_tiles()

    def spawn_random(self):
        tile_position = self.board.spawn_random_tile()
        if tile_position != None:
            tile = Square(
                self.surface, tile_position[1]*150+5, tile_position[0]*150+5, (238, 228, 150), str(2))
            self.tiles.append(tile)
        else:
            pass

    def start_game(self):
        self.spawn_random()
        self.start_state = False

    def end_game(self):
        if self.current_score > self.highest_score:
            self.set_high_score(self.current_score)
            self.highest_score = self.current_score
        self.reset_game()

    def reset_game(self):
        self.board.reset_board()
        self.current_score = 0
        self.tiles = []
        self.start_state = True

    # def add_tile(self, tile):
    #     self.tiels.append(tile)

    # def remove_tile(self, tile):
    #     self.tiels.remove(tile)

    def key_movements(self, event):

        if self.check_game_over():
            self.game_window = 'game_over_window'
        elif event.key == pygame.K_LEFT:
            self.board.shift('left')
            self.generate_tiles()
            self.spawn_random()
            self.current_score = self.board.get_current_score()
            self.check_game_over()
        elif event.key == pygame.K_RIGHT:
            self.board.shift('right')
            self.generate_tiles()
            self.spawn_random()
            self.current_score = self.board.get_current_score()
            self.check_game_over()
        elif event.key == pygame.K_UP:
            self.board.shift('up')
            self.generate_tiles()
            self.spawn_random()
            self.current_score = self.board.get_current_score()
            self.check_game_over()
        elif event.key == pygame.K_DOWN:
            self.board.shift('down')
            self.generate_tiles()
            self.spawn_random()
            self.current_score = self.board.get_current_score()
            self.check_game_over()

    def generate_tiles(self):
        self.tiles = []
        for row in range(self.board.get_board_len()):
            for column in range(len(self.board.board[row])):
                if not self.board.get_value_from_board(row, column) == 0:
                    tile = Square(self.surface, column*150+5, row*150+5, COLORS.get(
                        self.board.get_value_from_board(row, column), (0, 0, 0)), str(self.board.get_value_from_board(row, column)))

                    self.tiles.append(tile)

    def draw_tiles(self):
        for tile in self.tiles:
            tile.draw_rectangle()

    def get_high_score(self):
        try:
            db = shelve.open('score.txt')
            score = db['score']
            db.close()
            return int(score)
        except:
            db.close()
            self.set_high_score(0)
            score = 0
            return int(score)

    def set_high_score(self, score):
        db = shelve.open('score.txt')
        db['score'] = score
        db.close()

    def check_game_over(self):
        if self.board.is_board_full():
            if self.board.still_more_moves():
                return False
            else:
                self.game_window = 'game_over_window'
                return True
