import pygame
from math import *


SCREEN_SIZE = (1280, 720)
LINE_COLOR = (255, 0, 0)
POINT_COLOR = (0, 255, 0)


class Function(object):
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.rect = self.screen.get_rect()
        self.ratio = 10

    def start(self):
        self.update()
        while True:
            pygame.time.Clock().tick(60)
            self.event()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.ratio *= 1.2
                elif event.button == 5:
                    self.ratio /= 1.2
                self.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, LINE_COLOR, (0, self.rect.centery), (self.rect.width, self.rect.centery), 2)
        pygame.draw.line(self.screen, LINE_COLOR, (self.rect.centerx, 0), (self.rect.centerx, self.rect.height), 2)
        point_list = []
        for i in range(-self.rect.centerx, self.rect.centerx):
            for j in range(1, 10):
                x = i + j * 0.1
                y = sin(x)/x
                if -self.rect.centerx < x < self.rect.centerx and -self.rect.centery < y < self.rect.centery:
                    point_list.append((self.rect.centerx+x*self.ratio, self.rect.centery-y*self.ratio))
        pygame.draw.lines(self.screen, POINT_COLOR, False, point_list, 2)

    def update(self):
        self.draw()
        pygame.display.update()


if __name__ == '__main__':
    function = Function()
    function.start()
