#reporting and initialising pygame
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((500,500))


ball=pygame.draw.circle(screen,"red",(245,370),30)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    pygame.draw.circle(screen,"red",(245,370),30)   
    pygame.display.update()