import pygame
from pygame.locals import *
from random import*
import time
from carClass import*
import math


pygame.init()
pygame.display.set_caption("vroom") 

white = (255,255,255)
wind = pygame.display.set_mode((750, 1050))
timer = pygame.time.Clock()

surface = pygame.display.set_mode((1050,750))

background = pygame.image.load("course.png")
background = pygame.transform.scale(background,(1050,750))

ImageCar = pygame.image.load("voiturecompet.png")
ImageCar.set_colorkey(white)
ImageCar = pygame.transform.scale(ImageCar,(75,50))

car_rect = ImageCar.get_rect()

testt = pygame.display.get_surface()
pixArray = pygame.PixelArray(testt)
print(pixArray)


def drawVoiture(c,angleRotate):
    car_rect.center = (c.pos[0], c.pos[1])
    global ImageCar
    newImage = pygame.transform.rotate(ImageCar, angleRotate)
    newrect = newImage.get_rect()
    newrect.center = car_rect.center
    surface.blit(newImage, newrect)

def init():
    test = pygame.surfarray.array2d(background)
    print(test[0][0])

def main():
    c = car()
    tmpAngleRotat = 0
    tmp = 0
    window = False
    #pygame.key.set_repeat(1,20)
    while window == False:
        tmp += timer.tick_busy_loop() #update timer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window = True
                pygame.QUIT
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_d:
                    c.tournerD()               

                elif event.key == K_q:
                    c.tournerG()

                elif event.key == K_z:
                    c.accel()

                elif event.key == K_s:
                    c.frein()

     #   if tmp > 1000:
      #      #c.moove([c.pos[0]-50, c.pos[1]+25])
       #     global ImageCar
            #ImageCar = pygame.transform.rotate(ImageCar, 45)
        #    car_rect = ImageCar.get_rect()
         #   car_rect.center = (c.pos[0],c.pos[1])
          #  tmp = 0

    #    check = car_rect.center
    #    while(True):
    #        check = (check[0]-1,check[1])
    #        if surface.get_at(check) == (0,0,0):
    #            break

        surface.blit(background,(0,0))
        c.moove()   
        drawVoiture(c,c.angle)
        #pygame.draw.line(surface, (255,0,0), car_rect.center, check)
        pygame.display.flip()
        timer.tick(30)

#init()
main()

#pos = (pos + vectAngle*vitesse)
