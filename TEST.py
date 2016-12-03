import pygame
import square

pygame.init()
screen = pygame.display.set_mode((800,500))
square = square.square(screen)
clock = pygame.time.Clock()
isRunning = True

while isRunning:
    
    for event in pygame.event.get():
        square.clear()
        mousePressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            isRunning = False
        if mousePressed[0]:
            (x,y) = pygame.mouse.get_pos()
            square.draw(x,y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

pygame.quit()
quit()
