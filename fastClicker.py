import pygame
import time
from random import randint

pygame.init()

# Create a window
background = (200, 255, 255)
main_window = pygame.display.set_mode((500, 500))
main_window.fill(background)

#Game Timer
clock = pygame.time.Clock()
start_time = time.time()
current_time = start_time

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

# Label Class
class Label(Area):
    def setText(self, texts, fsize=12, textColor=(0,0,0)):
        self.image = pygame.font.SysFont("Verdana", fsize).render(texts, True, textColor)

    def draw(self, shift_x=0, shift_y=0):
        self.fillColor()
        main_window.blit(self.image, (self.rectangle.x + shift_x, self.rectangle.y + shift_y))

num_cards = 4
x = 70
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
cards = []
for num in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.setOutline(BLUE, 10)
    new_card.setText("CLICK", 26)
    cards.append(new_card)
    x += 100

RED = (255, 0, 0)
GREEN = (0, 255, 51)

ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)

LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)

wait = 0
points = 0

time_text = Label(0, 0, 50, 50, background)
time_text.setText("Time:", 40, DARK_BLUE)
time_text.draw(20, 20)

timer_text = Label(50, 55, 50, 50, background)
timer_text.setText("0:", 40, DARK_BLUE)
timer_text.draw(20, 20)

point_text = Label(345, 0, 50, 50, background)
point_text.setText("Points:", 40, DARK_BLUE)
point_text.draw(20, 20)

point_text = Label(345, 55, 50, 50, background)
point_text.setText("0", 40, DARK_BLUE)
point_text.draw(20, 20)

while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range (num_cards):
            cards[i].setColor((255, 255, 0))
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fillColor()

    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame. MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].setColor(GREEN)
                        points +=1
                    else:
                        cards[i].setColor(RED)
                        points -=1
                    cards[i].fillColor()
                    point_text.setText(str(points), 40, DARK_BLUE) 
                    point_text.draw (0, 0)

            

    new_time = time.time()
    if new_time - start_time >= 11:
        time_up = Label(0, 0, 500, 500, LIGHT_RED)
        time_up.setText("TIME IS UP !!!", 60, DARK_BLUE)
        time_up.draw(110, 110)
        break


    if int(new_time) - int(current_time) == 1:
        timer_text.setText(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer_text.draw(0.0)
        current_time = new_time

    if points >= 5:
        time_up = Label(0, 0, 500, 500, LIGHT_GREEN)
        time_up.setText("YOU WON!!!", 60, DARK_BLUE)
        time_up.draw(110, 110)
        break

    pygame.display.update()
    clock.tick(40)
pygame.display.update()






M