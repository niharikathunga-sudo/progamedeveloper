#reporting and initialising pygame
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((500,500))

#create a square class
class circles:
    def __init__(self,color,pos,radius,width=0):
        self.screen=screen
        self.color=color
        self.pos=pos
        self.radius=radius
        self.width=width
        

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)
    def grow(self):
        self.radius+=10
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)

#creating instances

circ1=circles("light blue",(10,70),50,10)
circ2=circles("light pink",(90,230),70,45)
circ3=circles("light green",(245,370),30,73)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            circ1.draw()
            circ2.draw()
            circ3.draw()
        elif event.type==pygame.MOUSEBUTTONUP:
            circ1.grow()
            circ2.grow()
            circ3.grow()
        elif event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circ4=circles("light yellow",pos,5)
            circ4.draw()
    
        pygame.display.update()