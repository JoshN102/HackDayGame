import pygame

class mob:
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def draw(self,x,y,screen):
        #Temporary mobs until I implement sprites
        pygame.draw.circle(screen,(0,128,255),(x,y),5)
        
    def clear(self):
        #Temp until sprites
        pygame.display.fill((0,0,0))
        
    def check_health(self):
        if self.health <= 0:
            self.clear()
        else:
            pass
        
    def move(self,x,y):
        pass
    
class player:
    
    def __init__(self,origin,speed):
        (self.x,self.y) = origin
        self.speed = speed
        
    def move(self,direction):
        #direction is "right","left","up" or "down"
        if direction == "right":
            self.x += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "up":
            self.y -= self.speed
        else:
            self.y += self.speed
            
    def draw(self,screen):
        #temp
        pygame.draw.circle(screen,(0,128,255),(self.x,self.y),20)
        
    def get_XY(self):
        return (self.x,self.y)
        
    
    
    
        
        
        
        
        
        