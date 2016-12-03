import pygame
import math


class bullet2:
    
    def __init__(self,screen,xOrigin,yOrigin):
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        self.x = xOrigin
        self.y = yOrigin
        self.screen = screen
        
    def draw(self,x,y,radius):
        pygame.draw.circle(self.screen,(0,128,255),(math.floor(x),math.floor(y)),radius)
        
    def clear(self):
        self.screen.fill((0,0,0))
        
    def fire(self,xTarget,yTarget):
        xChange = (xTarget-self.xOrigin)
        yChange = (yTarget-self.yOrigin)
        change = math.sqrt(xChange**2 + yChange**2)
        angle = math.atan(yChange/xChange)
        travelled = math.sqrt(((self.x-self.xOrigin)**2)+((self.y-self.yOrigin)**2))
        
        if travelled < change:
            self.draw(self.x,self.y,2)
            self.x += math.cos(angle)
            self.y += math.sin(angle)
        else:
            self.clear()
            
        pygame.display.flip()
        