import pygame
from fastClicker import main_window



#Area Class
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rectangle = pygame.Rect (x, y, width, height)
        self.fill_color = color

    def setColor(self, new_color):
        self.fill_color = new_color

    def fillColor(self): #Draw the rectangle on the main window
        pygame.draw.rect(main_window, self.fill_color, self.rectangle)

    def setOutline(self, frame_color, thickness): #Set the outline color
        pygame.draw.rect(main_window, frame_color, self.rectangle, thickness)

    def collidepoint(self, x, y):
        return self.rectangle.collidepoint(x, y)
