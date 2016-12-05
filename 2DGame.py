import pygame
import bullet
import mob
pygame.init()

def main():
    
    player = mob.player((0,0),3)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,500))
    bullets = []
    isRunning = True
    
    while isRunning:
        
        screen.fill((0,0,0))
        #Check for input
        for event in pygame.event.get():
            #exit button
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
            #key input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    isRunning = False

            #mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                target = pygame.mouse.get_pos()
                bullets.append(bullet.bullet(player.get_XY(),3,target))
                
        key = pygame.key.get_pressed()
        if key[pygame.K_d]: player.move("right")
        if key[pygame.K_s]: player.move("down")
        if key[pygame.K_a]: player.move("left")
        if key[pygame.K_w]: player.move("up")
        
        #Events
        player.draw(screen)
        for aBullet in bullets:
            aBullet.draw(screen)
            aBullet.move()

        #display
        pygame.display.flip()
        
        #Frames
        clock.tick(30)
        
        
main()