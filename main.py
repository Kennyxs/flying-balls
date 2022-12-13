import pygame

class Game:
    def __init__(self, height,weidth,  mappng) -> None:
        self.height = height
        self.weidth = weidth
        self.surface = pygame.display.set_mode((self.height, self.weidth))
    def new(self):
        self.fps = pygame.time.Clock() 
        
    def events(self):
        events = pygame.event.get()
        stop = 1
        for e_now in events:
            if e_now.type == pygame.constants.QUIT:
                stop = -1
            else:
                stop = 1
        return stop
    def update(self):
        
        pygame.display.update()

    def draw(self):
        self.surface.fill((0,0,0))
        
    def run(self):
        stop = 1
        self.new()
        while stop > 0:
            stop = self.events()
            self.draw()
            self.update()
            self.fps.tick(60)
