#reporting and initialising pygame
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((500,500))

#create a square class
class squares:
    def __init__(self,color,dimensions):
        self.screen=screen
        self.color=color
        self.dimensions=dimensions

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.dimensions)

#creating instances

rect1=squares("light blue",(10,70,100,130))
rect2=squares("light pink",(90,230,170,130))
rect3=squares("light green",(245,370,80,110))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("black")
    rect1.draw()
    rect2.draw()
    rect3.draw()
    pygame.display.update()