import pygame

class square:

    def __init__(self,screen):
        self.screen = screen
        
    def draw(self,x,y):
        rect = pygame.rect = (x,y,100,100)
        pygame.draw.rect(self.screen,(0,128,255),rect)
        pygame.display.flip()
            
    def clear(self):
        self.screen.fill((0,0,0))