import pygame
from sprites import *
import random
class Game:
    def __init__(self, height,weidth) -> None:
        self.height = height
        self.weidth = weidth
        self.surface = pygame.display.set_mode((self.height, self.weidth))
    def new(self):
        self.fps = pygame.time.Clock() 
        self.player = Playerellipse()
        self.coordplayer = self.player.coordinats
        self.group = Group()
        self.test_event = pygame.USEREVENT
        pygame.time.set_timer(self.test_event, 2000)
        self.mousecord = []
    def events(self):
        events = pygame.event.get()
        stop = 1
        for e_now in events:
            if e_now.type == self.test_event:
                evil = Evilellipse(self.coordplayer)
                self.group.append(evil)
            if e_now.type == pygame.MOUSEBUTTONDOWN:
                # self.mousecord = pygame.mouse.get_pos
                self.mousecord = e_now.pos
                self.player.update(self.mousecord)
                print(self.mousecord)
            if e_now.type == pygame.constants.QUIT:
                stop = 0
        return stop
    def update(self):
        pygame.display.update()
        self.group.update()
        

    def drawing(self):
        self.surface.fill((0,0,0))
        self.player.draw(self.surface)
        self.group.draw(self.surface)

    def first_draw(self):
        evil = Evilellipse(self.coordplayer)
        self.group.append(evil)

    def run(self):
        skolko = random.randint(1,29)
        f =1
        stop = 1
        self.new()
        while f<=skolko:
            self.first_draw()
            f+=1
        while stop > 0:
            stop = self.events()
            self.drawing()
            self.update()
            self.group.delete(self.player.rect)
            self.fps.tick(60)


game = Game(WEIDTH, HEIGHT)
game.run()