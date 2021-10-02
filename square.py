import pygame
from pygame.font import Font

size = 150

FONT_COLORS = {
    0: (119, 110, 101),
    1: (249, 246, 242)
}


class Square:
    # Initializing the Sqaure class:
    # settings the surface, x_position, y_position, color & value"number"
    def __init__(self, surface, x, y, color, value):
        self.surface = surface
        self.x_position = x
        self.y_position = y
        self.color = color
        self.value = value
        self.font_color = None

    # Drawing the rectangle on the surface and bliting the value on it

    def draw_rectangle(self):
        if int(self.value) > 4:
            self.font_color = FONT_COLORS.get(1)
        else:
            self.font_color = FONT_COLORS.get(0)

        self.font = pygame.font.SysFont('Arial', 70).render(
            self.value, True, self.font_color)
        self.rect = pygame.Rect(
            self.x_position, self.y_position, 140, 140)
        rect_obj = pygame.draw.rect(self.surface, self.color, self.rect)
        center_cords = self.font.get_rect(center=rect_obj.center)
        self.surface.blit(self.font, center_cords)

    # Setting rect value
    def set_rect_value(self, value):
        self.value = value

    # Getting rect values for sum purposes
    def get_rect_value(self):
        return self.value

    # # Move rectangle around
    # def move(self, direction):
    #     if direction == 'left':
    #         self.x_position -= 150
    #     elif direction == 'right':
    #         self.x_position += 150
    #     elif direction == 'up':
    #         self.y_position -= 150
    #     elif direction == 'down':
    #         self.y_position += 150
