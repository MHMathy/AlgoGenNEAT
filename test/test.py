import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
pos = [400,50]
#pygame.key.set_repeat(0)
background_image = pygame.image.load("course.png").convert()
while not done:
    events = pygame.event.get()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_q:
                pos[0] -= 10
            if event.key == pygame.K_d:
                pos[0] += 10
            if event.key == pygame.K_z:
                pos[1] -= 10
            if event.key == pygame.K_s:
                pos[1] += 10
    pos[1] +=1




    screen.blit(background_image,(0,0))
    pygame.draw.circle(screen,(255,0,0),(pos[0],pos[1]),20)
    pygame.display.flip()
pygame.quit()
quit()
