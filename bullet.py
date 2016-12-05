import pygame
import math

class bullet(pygame.sprite.Sprite):
    
    def __init__(self,origin,speed,target):
        [self.x,self.y] = origin
        self.origin = origin
        self.spd = speed
        self.target = target
        self.surf = pygame.Surface((3,3))
        self.surf.fill((200,200,200))
        self.rect = self.surf.get_rect(center=(self.x,self.y))
        
    def move(self):
        (xTarget,yTarget) = self.target
        xChange = xTarget - self.origin[0]
        yChange = yTarget - self.origin[1]
        distance = math.sqrt((yChange**2)+(xChange**2))
        travelled = math.sqrt(((self.x-self.origin[0])**2)+((self.y-self.origin[1])**2))
        try:
            angle = math.atan(yChange/xChange)
        except ZeroDivisionError:
            return 0
        if travelled < distance:
            if xChange >= 0:
                self.x += self.spd*math.cos(angle)
                self.y += self.spd*math.sin(angle)
                self.rect = self.surf.get_rect(center=(self.x,self.y))
            else:
                self.x -= self.spd*math.cos(angle)
                self.y -= self.spd*math.sin(angle)  
                self.rect = self.surf.get_rect(center=(self.x,self.y))
        else:
            return 0
            
    def draw(self,screen):
        screen.blit(self.surf,(self.x,self.y))
        
    def get_XY(self):
        return (self.x,self.y)
        