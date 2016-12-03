import pygame
import square

pygame.init()
screen = pygame.display.set_mode((800,500))
square = square.square(screen)
clock = pygame.time.Clock()
isRunning = True

shape = 's'
while isRunning:
    
    for event in pygame.event.get():
        square.clear()
        mousePressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_s:
                shape = 's'
            elif event.key == pygame.K_c:
                shape = 'c'
            elif event.key == pygame.K_t:
                shape = 't'
        if mousePressed[0]:
            (x, y) = pygame.mouse.get_pos()
            square.draw(x, y, shape)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
