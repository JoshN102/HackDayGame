import pygame
import random

class mob(pygame.sprite.Sprite):
    
    def __init__(self,origin,speed,health):
        LENGTH = 25
        (self.x,self.y) = origin
        self.speed = speed
        self.health = health
        super(mob,self).__init__()
        self.surf = pygame.Surface((LENGTH,LENGTH))
        self.rect = self.surf.get_rect(center=(self.x-LENGTH/2,self.y-LENGTH/2))
        
    def move(self,direction):
        if direction == "right":
            self.x += self.speed
            self.rect = self.surf.get_rect(center=(self.x,self.y))
        elif direction == "left":
            self.x -= self.speed
            self.rect = self.surf.get_rect(center=(self.x,self.y))
        elif direction == "up":
            self.y -= self.speed
            self.rect = self.surf.get_rect(center=(self.x,self.y))
        else:
            self.y += self.speed
            self.rect = self.surf.get_rect(center=(self.x,self.y))
        
    def get_XY(self):
        return (self.x,self.y)
        
    def check_health(self):
        if self.health <= 0:
            self.clear()
        else:
            pass
        
    def draw(self,screen,colour):
        self.surf.fill(colour)
        screen.blit(self.surf,(self.x,self.y))
        
class player(mob):
    pass
    
class enemy(mob):
    
    def path(self):
        direction = random.randint(1,60)
        if direction == 1:
            self.move("right")
        elif direction == 2:
            self.move("down")
        elif direction == 3:
            self.move("left")
        elif direction == 4:
            self.move("up")
        else:
            pass