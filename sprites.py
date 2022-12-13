import pygame

class ellise(pygame.sprite.Sprite):
    def __init__(self,x, y, size ) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.rect.Rect(self.x, self.y,self.size, self.size)
    def draw(self, surface):
        pygame.draw.ellipse(surface,[0,0,0],self.rect)
    def update(self):
        break

class Playerellipse(ellise):
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size
        super().__init__(x, y, size)


class Evilellipse(ellise):
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size
        super().__init__(x, y, size)
   