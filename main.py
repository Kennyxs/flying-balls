import pygame
from sprites import *
import random
import pygame.freetype
from settings import*
pygame.init()
class Game:
    def __init__(self, height,weidth) -> None:
        self.height = height
        self.weidth = weidth
        self.surface = pygame.display.set_mode((self.height, self.weidth))
    def new(self):
        self.fps = pygame.time.Clock() 
        self.player = Playerellipse(color = COLOR)
        self.coordplayer = self.player.coordinats
        self.group = Group()
        self.test_event = pygame.USEREVENT
        pygame.time.set_timer(self.test_event, 500)
        self.mousecord = [WEIDTH//2, HEIGHT//2]
    def events(self):
        events = pygame.event.get()
        stop = 1
        for e_now in events:
            if e_now.type == self.test_event:
                evil = Evilellipse(self.coordplayer)
                self.group.append(evil)
            if e_now.type == pygame.MOUSEBUTTONDOWN:
                pass
                # self.mousecord = e_now.pos
            if e_now.type == pygame.constants.QUIT:
                stop = 0
        return stop
    def update(self):
        pygame.display.update()
        self.group.update()
        self.mousecord = pygame.mouse.get_pos()
        self.player.update(self.mousecord)

    def drawing(self):
        self.surface.fill((0,0,0))
        self.player.draw(self.surface)
        self.group.draw(self.surface)

    def first_draw(self):
        skolko = MANYENEMY
        f = 1
        while f<=skolko:
            evil = Evilellipse(self.coordplayer)
            self.group.append(evil)
            f+=1

    def remenurer(self):
        self.group.stop = 1
        self.player = Playerellipse()
        self.group.clear()
        self.first_draw()

        

    def menuu(self):
        
        shrift = pygame.freetype.Font(None,20)
        
        colorr = WHITE 
        color = GREY
        m = 1
    
        while m > 0:
            
            events = pygame.event.get()
            for e_now in events:
                if e_now.type == pygame.constants.QUIT:
                    return False
                if e_now.type == pygame.constants.KEYDOWN:
                    if e_now.key == pygame.K_RETURN:
                        if color == WHITE:
                            return False
                    if e_now.key == pygame.K_RETURN:
                        if colorr == WHITE:
                            return True
                    if e_now.key == pygame.K_DOWN:
                        colorr  =  GREY
                        color = WHITE
                    if e_now.key == pygame.K_UP:
                        colorr  =  WHITE
                        color = GREY
            self.surface.fill(BLUE)
            shrift.render_to(self.surface,(40,40),"Play",  colorr)
            shrift.render_to(self.surface,(40,90),"Quit", color )
            
            
            # self.surface.blit(renderr, [10,10])
            # self.surface.blit(render, [60,60])
            pygame.display.update()
        
    def win_lose(self):
        shrift = pygame.freetype.Font(None,90)
        if self.player.rect.height>200:
            shrift.render_to(self.surface,(40,40),"u win",  WHITE)
            print("win")
            return 0
        else:
            return 1

    def run(self):
        
        
        stop = self.menuu()
        self.new()
        self.first_draw()
        while stop > 0:
            stop = self.events()
            self.drawing()
            self.update()
            
            if self.group.stop != 1 or self.win_lose() !=1:
                stop = self.menuu()
                self.remenurer()
                
            sizeup = self.group.delete(self.player.rect)
            self.player.rect.width +=sizeup
            self.player.rect.height +=sizeup
            self.fps.tick(60)


game = Game(WEIDTH, HEIGHT)
game.run()