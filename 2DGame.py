import pygame
import bullet
import mob
import random
pygame.init()

def main():
    WIDTH = 500
    HEIGHT = 800
    player = mob.player((0,0),6,10)
    clock = pygame.time.Clock()
    enemy = mob.enemy((HEIGHT/2,WIDTH/2),3,10)
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    
    bullets = []

    isEnemy = True
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
        surf = pygame.Surface(screen.get_size())
        surf.fill((150,0,50))
        screen.blit(surf, (0,0))
        player.draw(screen,(0,128,255))
        if isEnemy: 
            enemy.draw(screen,(0,255,0))
            enemy.path()
        for aBullet in bullets:
            if aBullet.move() == 0:
                pass
            else:
                aBullet.draw(screen)
                aBullet.move()
                if pygame.sprite.collide_rect(enemy,aBullet):
                    yEnemy = random.randint(1,HEIGHT)
                    xEnemy = random.randint(1,WIDTH)
                    enemy = mob.enemy((yEnemy,xEnemy),3,10)

        #display
        pygame.display.flip()
        
        #Framess
        clock.tick(30)
        
        
main()