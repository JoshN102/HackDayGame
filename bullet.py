import pygame
import math

class bullet:
    
    def __init__(self,origin,speed,target):
        [self.x,self.y] = origin
        self.origin = origin
        self.spd = speed
        self.target = target
        
    def move(self):
        (xTarget,yTarget) = self.target
        xChange = xTarget - self.x
        yChange = yTarget - self.y
        distance = math.sqrt((yChange**2)+(xChange**2))
        travelled = math.sqrt(((self.x-self.origin[0])**2)+((self.y-self.origin[1])**2))
        try:
            angle = math.atan(yChange/xChange)
        except ZeroDivisionError:
            return 0
        if travelled < distance:
            self.x += self.spd*math.cos(angle)
            self.y += self.spd*math.sin(angle)
        else:
            return 0
            
    def draw(self,screen):
        pygame.draw.circle(screen,(0,128,255),(int(math.floor(self.x)),int(math.floor(self.y))),4)
        