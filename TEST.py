import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))

clock = pygame.time.Clock()
isRunning = True

while isRunning == True: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            rect = pygame.rect = (x,y,100,100)
            pygame.draw.rect(screen,(0,128,255),rect)
            pygame.display.flip()
            clock.tick(30)
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0,0,0))

                