import config
import levels
import pygame

class Level():
    def __init__(self, level_n):
        self.work = True
        self.n = config.N
        self.cell_size = config.CELL_SIZE
        self.matrix = levels.test
        self.top = self.left = 50

    def render(self, screen):
        for row in range(self.n):
            for column in range(self.n):
                cell = self.matrix[row][column]
                rect = pygame.Rect(self.cell_size * column + self.left, self.cell_size * row + self.top, 
                                   self.cell_size, self.cell_size)
                pygame.draw.rect(screen, config.render_rulls[cell], rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)