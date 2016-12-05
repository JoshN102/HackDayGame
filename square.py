import pygame

class square:


    def __init__(self,screen):
        self.screen = screen
        
    def draw(self, x, y, shape):
        rect = pygame.rect = (x- 50, y- 50, 100, 100)
        if shape == 's':
            pygame.draw.rect(self.screen,(0, 128, 255), rect)
        elif shape == 'c':
            pygame.draw.circle(self.screen, (0, 128, 255), (x, y), 50)
        elif shape == 't':
            vertices = ((x, y - 50), (x + 100/(3**0.5), y + 50), (x - 100/(3**0.5), y + 50))
            pygame.draw.polygon(self.screen, (0, 128, 255), vertices)
    def clear(self):
        self.screen.fill((0,0,0))