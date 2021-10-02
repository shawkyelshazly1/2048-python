from game import Game
import pygame
import sys
HEIGHT = 600
WIDTH = 600
pygame.init()


class Game_GUI:
    def __init__(self, width, height):
        self.window_w = width
        self.window_h = height
        self.windowClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.window_w, self.window_h))
        self.game = Game(self.screen)
        pygame.display.set_caption("2048 - Game")

        self.Main_run()

    def Main_run(self):
        while True:
            self.screen.fill((205, 193, 180))
            self.draw_borders()
            self.game.run()
            pygame.display.update()
            self.windowClock.tick(120)

    # Draw grid borders 5*5
    def draw_borders(self):
        for x in range(0, self.window_w, 150):
            for y in range(0, self.window_h, 150):
                rect = pygame.Rect(x, y, 150, 150)
                pygame.draw.rect(self.screen, (187, 173, 160), rect, 10)


if __name__ == '__main__':

    Game_GUI(WIDTH, HEIGHT)
