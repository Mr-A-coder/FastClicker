import pygame
from area import Area
from fastClicker import main_window

# Label Class
class Label(Area):
    def setText(self, texts, fsize=12, textColor=(0,0,0)):
        self.image = pygame.font.SysFont("Verdana", fsize).render(texts, True, textColor)

    def draw(self, shift_x=0, shift_y=0):
        self.fillColor()
        main_window.blit(self.image, (self.rectangle.x + shift_x, self.rectangle.y + shift_y))