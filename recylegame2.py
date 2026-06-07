import pygame,random,time
pygame.init()
screen=pygame.display.set_mode((864,750))
clock=pygame.time.Clock()
pygame.display.set_caption("Welcome!!!")
score=0
start_time=time.time()
#font print score
font=pygame.font.SysFont("Pacifico",20)
text=font.render("score"+str(score),True,"black")

class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(40,50))
        self.rect=self.image.get_rect()


class recycleable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class nonrecycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plasticbag.png")
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()


recycleable1=["pencil.png","box.png","paper.png"]


#create sprite groups

r_group=pygame.sprite.Group()
nr_group=pygame.sprite.Group()
all_group=pygame.sprite.Group()

for i in range(50):
    item=recycleable(random.choice(recycleable1))
    item.rect.x=random.randrange(844)
    item.rect.y=random.randrange(730)
    r_group.add(item)
    all_group.add(item)

for i in range(20):
    plastic=nonrecycleable()
    plastic.rect.x=random.randrange(844)
    plastic.rect.y=random.randrange(730)
    nr_group.add(plastic)
    all_group.add(plastic)

trash=bin()
all_group.add(trash)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    past=time.time()-start_time
    if past>=60:
        if score>30:
            text=font.render("TIME UP!! YOU WON!!",True,"black")
            screen.fill("light green")
        else:
            text=font.render("TIME UP!!! YOU LOST!!",True,"black")
            screen.fill("white")
        screen.blit(text,(125,467))

    else:
        screen.fill("light pink")
        text=font.render("Time "+str(round(past,0)),True,"black")
        screen.blit(text,(50,50))

        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP] and trash.rect.y>0:
            trash.rect.y-=5
        if keys[pygame.K_DOWN] and trash.rect.y<720:
            trash.rect.y+=5
        if keys[pygame.K_LEFT] and trash.rect.x>0:
            trash.rect.x-=5
        if keys[pygame.K_RIGHT] and trash.rect.x<844:
            trash.rect.x+=5

        #check for collision
        rhitlist=pygame.sprite.spritecollide(trash,r_group,True)
        nrhitlist=pygame.sprite.spritecollide(trash,nr_group,True)

        for item in rhitlist:
            score+=1

        for item in nrhitlist:
            score-=2
        
        text=font.render("Score "+str(score),True,"black")
        screen.blit(text,(50,90))


            
        



    all_group.draw(screen)
    pygame.display.update()