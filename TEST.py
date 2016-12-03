import pygame
import square

pygame.init()
screen = pygame.display.set_mode((800,500))
square = square.square(screen)
clock = pygame.time.Clock()
isRunning = True

while isRunning == True: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            square.draw(x,y)
            clock.tick(30)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
        if event.type == pygame.MOUSEBUTTONUP:
            square.clear()

pygame.quit()
quit()
