import pygame,random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE GETS INVADED... OR DOES IT?")

bot1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot1.png"),(50,50)),90)
bot2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bot2.png"),(50,50)),270)
bg=pygame.image.load("spaceeeeeee.png")
border=pygame.Rect(400,0,25,600)

class bots(pygame.sprite.Sprite):
    def __init__(self,x,y,image,contols,side)