import pygame
import square
import bullet2

pygame.init()
screen = pygame.display.set_mode((800,500))
square = square.square(screen)
clock = pygame.time.Clock()
isRunning = True

bullet = bullet2.bullet2(screen,0,0)

while isRunning == True: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            bullet.fire(x,y)
            print(str(x)+ "  " +str(y))
            print("Working so far")
#            square.draw(x,y,100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
        if event.type == pygame.MOUSEBUTTONUP:
#            square.clear()
             pygame.display.flip()
        clock.tick(30)
pygame.quit()
quit()
        
    