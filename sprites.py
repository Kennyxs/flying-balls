import pygame
import random
from settings import *

class ellise(pygame.sprite.Sprite):
    def __init__(self, x, y, size ) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.rect.Rect(self.x, self.y,self.size, self.size)
    def draw(self, surface):
        pygame.draw.ellipse(surface,[0,0,0],self.rect)
    def update(self):
        pass

class Playerellipse(ellise):
    def __init__(self,color = WHITE) -> None:
        self.size = random.randint(10,20)
        self.coordinats = [WEIDTH//2,HEIGHT//2]
        self.color = color
        self.rect = pygame.rect.Rect(self.coordinats[0], self.coordinats[-1],self.size, self.size)
        self.rect.center = [self.coordinats[0], self.coordinats[-1]]
        
    def draw(self,surface):
        pygame.draw.ellipse(surface,self.color,self.rect)
    def update(self,mousecord):
        # print(list(mousecord))
        self.rect.center = list(mousecord)
    

class Evilellipse(ellise):
    def __init__(self,coordplayer) -> None:
        self.size = random.randint(10,100)
        self.speedy = 0
        self.speedx = 0
        self.coordplayer = coordplayer
        self.coordinatx = 0
        self.coordinaty = 0
        self.walls = random.randint(1,4)
        self.colliders()
        self.color = COLOURS[random.randint(0,len(COLOURS)-1)]
        self.rect = pygame.rect.Rect(self.coordinatx, self.coordinaty,self.size, self.size)
        self.rect.center = [self.coordinatx, self.coordinaty]
        self.groups = []
        self.gameon = 1
        
    def colliders(self):
        if self.walls == 1: #left
            self.coordinatx = 0
            self.coordinaty = random.randint(0,HEIGHT-1) 
            self.speedx = random.randint(1,2)
            self.speedy = random.choice([random.randint(-2,-1),random.randint(1,2)])
        if self.walls == 2: #right
            self.coordinatx = WEIDTH - 1
            self.coordinaty = random.randint(0,HEIGHT-1) 
            self.speedx = random.randint(-2,-1)
            self.speedy = random.choice([random.randint(-2,-1),random.randint(1,2)])
        if self.walls == 3: #up
            self.coordinatx = random.randint(0,WEIDTH-1) 
            self.coordinaty = 0
            self.speedx = random.choice([random.randint(-2,-1),random.randint(1,2)])
            self.speedy = random.randint(1,2) 
        if self.walls == 4: #down
            self.coordinatx = random.randint(0,WEIDTH-1) 
            self.coordinaty = HEIGHT-1
            self.speedx = random.choice([random.randint(-2,-1),random.randint(1,2)])
            self.speedy = random.randint(-2,-1) 
        
        

    def draw(self,surface):
        pygame.draw.ellipse(surface,self.color,self.rect)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx 

class Group(list):
    def __init__(self, *sprites):
        self.stop = 1
        super().__init__(sprites)
    def update(self):
        for up in self:
            up.update()

    def draw (self, surface):
        for dr in self:
            dr.draw(surface)
    def append(self, a):
        super().append(a)
        a.groups.append(self)
    def delete(self,playerrect): 
            #playerrect,playersize
        sizeup = 0
        for t in self:
            if pygame.Rect.colliderect(t.rect, playerrect):
                if playerrect.height > t.rect.height:
                    print("collide")
                    sizeup = t.size//4
                    self.remove(t)
                else:
                    self.stop=0
                    print('lose')
        return sizeup
             
                    


                