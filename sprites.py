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
    def __init__(self) -> None:
        self.size = random.randint(10,15)
        self.speedy = random.randint(-2,2)
        self.speedx = random.randint(-2,2)
        self.coordinats = DIFERENT[random.randint(0,3)]
        self.color = random.randint(0,len(COLOURS)-1)
        self.rect = pygame.rect.Rect(self.coordinats[0], self.coordinats[-1],self.size, self.size)
        self.rect.center = [self.coordinats[0], self.coordinats[-1]]
        
    def draw(self,surface):
        pygame.draw.ellipse(surface,self.color,self.rect)
    def update(self):
        pass

class Evilellipse(ellise):
    def __init__(self,coordplayer) -> None:
        self.size = random.randint(10,100)
        self.speedy = random.randint(-2,2)
        self.speedx = random.randint(-2,2)
        self.coordplayer = coordplayer
        self.coordinatx = 0
        self.coordinaty = 0
        self.colliders()
        self.color = COLOURS[random.randint(0,len(COLOURS)-1)]
        self.rect = pygame.rect.Rect(self.coordinatx, self.coordinaty,self.size, self.size)
        self.rect.center = [self.coordinatx, self.coordinaty]
        self.groups = []
        
    def colliders(self):
        if self.coordplayer == DIFERENT[0]:
            self.coordinatx = random.randint(0, WEIDTH -1) 
            self.coordinaty = random.randint(0, DIFERENT[1][-1] -1) 
        if self.coordplayer == DIFERENT[1]:
            self.coordinatx = random.randint(0, WEIDTH -1) 
            self.coordinaty = random.randint(DIFERENT[0][-1] -1,HEIGHT -1) 
        if self.coordplayer == DIFERENT[2]:
            self.coordinatx = random.randint(0, DIFERENT[3][0]-1) 
            self.coordinaty = random.randint(0, HEIGHT-1) 
        if self.coordplayer == DIFERENT[3]:
            self.coordinatx = random.randint(DIFERENT[2][0]-1,WEIDTH - 1 ) 
            self.coordinaty = random.randint(0, HEIGHT-1) 
        
        

    def draw(self,surface):
        pygame.draw.ellipse(surface,self.color,self.rect)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx 

class Group(list):
    def __init__(self, *sprites):
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