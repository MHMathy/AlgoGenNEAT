import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
pos = [400,50]
#pygame.key.set_repeat(0)
background_image = pygame.image.load("course.png").convert()
police = pygame.font.Font('../../data/arial_narrow_7.ttf', 27)
valTest = 45
texte = police.render("cc : "+ str(valTest), True, (255,255,255))

rectTest = pygame.Rect((400,100),(100,50))

while not done:
    events = pygame.event.get()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image,(0,0))
    screen.blit(texte,rectTest)
    pygame.display.flip()
pygame.quit()
quit()
