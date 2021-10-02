import time
from pygame.constants import SRCALPHA
from game import Game
import pygame
import sys
HEIGHT = 700
WIDTH = 600
pygame.init()


class Game_GUI:
    def __init__(self, width, height):

        self.window_w = width
        self.window_h = height
        self.windowClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.window_w, self.window_h))
        self.game = Game(self.screen)
        pygame.display.set_caption("2048 - Game")

        self.Main_run()

    def Main_run(self):

        while True:
            if self.game.game_window == 'menu_window':
                self.main_menu()
            elif self.game.game_window == 'game_window':
                self.draw_scores_on_screen()
                self.draw_borders()
                self.game.run()
            elif self.game.game_window == 'game_over_window':
                time.sleep(1)
                self.game_over_screen()

            pygame.display.update()
            self.windowClock.tick(120)

    # Draw grid borders 5*5

    def draw_borders(self):
        for x in range(0, self.window_w, 150):
            for y in range(100, self.window_h, 150):
                rect = pygame.Rect(x, y, 150, 150)
                pygame.draw.rect(self.screen, (187, 173, 160), rect, 10)

    def main_menu(self):
        self.game.end_game()
        self.screen.fill((250, 248, 239))
        self.font = pygame.font.SysFont('Dyuthi', 50).render(
            "Welcome To 2048", True, (119, 110, 101))
        text_rect = self.font.get_rect(center=(WIDTH/2, HEIGHT/2-50))
        self.screen.blit(self.font, text_rect)

        self.font2 = pygame.font.SysFont('Verdana', 30).render(
            "Press [Space] To Start", True, (119, 110, 101))
        text_rect2 = self.font2.get_rect(center=(WIDTH/2, HEIGHT/2+10))
        self.screen.blit(self.font2, text_rect2)

        self.font3 = pygame.font.SysFont('Purisa', 30).render(
            "Highest Score", True, (119, 110, 101))
        text_rect3 = self.font3.get_rect(center=(WIDTH/2, HEIGHT/2+100))
        self.screen.blit(self.font3, text_rect3)

        self.font4 = pygame.font.SysFont('Purisa', 45).render(
            str(self.game.highest_score), True, (119, 110, 101))
        text_rect4 = self.font4.get_rect(center=(WIDTH/2, HEIGHT/2+150))
        self.screen.blit(self.font4, text_rect4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.game_window = 'game_window'
                    self.game.end_game()

    def draw_scores_on_screen(self):
        self.screen.fill((205, 193, 180))
        self.font5 = pygame.font.SysFont('Dyuthi', 30).render(
            "Highest Score", True, (119, 110, 101))
        text_rect5 = self.font5.get_rect(center=(450, 25))
        self.screen.blit(self.font5, text_rect5)

        self.font6 = pygame.font.SysFont('Dyuthi', 35).render(
            str(self.game.highest_score), True, (119, 110, 101))
        text_rect6 = self.font6.get_rect(center=(450, 60))
        self.screen.blit(self.font6, text_rect6)

        self.font7 = pygame.font.SysFont('Dyuthi', 30).render(
            "Current Score", True, (119, 110, 101))
        text_rect7 = self.font7.get_rect(center=(150, 25))
        self.screen.blit(self.font7, text_rect7)

        self.font8 = pygame.font.SysFont('Dyuthi', 35).render(
            str(self.game.current_score), True, (119, 110, 101))
        text_rect8 = self.font8.get_rect(center=(150, 60))
        self.screen.blit(self.font8, text_rect8)

    def game_over_screen(self):

        self.screen.fill((238, 228, 218))

        self.font12 = pygame.font.SysFont('Purisa', 90).render(
            "Game Over", True, (119, 110, 101))
        text_rect12 = self.font12.get_rect(
            center=(WIDTH/2, HEIGHT/2-120))
        self.screen.blit(self.font12, text_rect12)

        self.font13 = pygame.font.SysFont('Dyuthi', 50).render(
            "YOur Score", True, (119, 110, 101))
        text_rect13 = self.font13.get_rect(
            center=(WIDTH/2, HEIGHT/2))
        self.screen.blit(self.font13, text_rect13)

        self.font14 = pygame.font.SysFont('Dyuthi', 35).render(
            str(self.game.current_score), True, (119, 110, 101))
        text_rect14 = self.font14.get_rect(
            center=(WIDTH/2, HEIGHT/2+50))
        self.screen.blit(self.font14, text_rect14)

        self.font15 = pygame.font.SysFont('Dyuthi', 30).render(
            'Press [Escape] To Return To Main Menu', True, (119, 110, 101))
        text_rect15 = self.font15.get_rect(
            center=(WIDTH/2, HEIGHT/2+170))
        self.screen.blit(self.font15, text_rect15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_window = 'menu_window'


if __name__ == '__main__':

    Game_GUI(WIDTH, HEIGHT)
