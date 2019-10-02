import pygame
from pygame.locals import *
from random import*
import time
from carClass import*

pygame.init()
pygame.display.set_caption("vroom") 

white = (255,255,255)
wind = pygame.display.set_mode((750, 1050))
timer = pygame.time.Clock()

surface = pygame.display.set_mode((1050,750))

background = pygame.image.load("course.png")
background = pygame.transform.scale(background,(1050,750))

ImageCar = pygame.image.load("voiture.jpg")
ImageCar.set_colorkey(white)
ImageCar = pygame.transform.scale(ImageCar,(75,50))
car_rect = ImageCar.get_rect()

def main():
    c = car()
    car_rect.center = (c.pos[0], c.pos[1])
    tmp = 0
    window = False
    while window == False:
        tmp += timer.tick_busy_loop() #update timer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window = True
                pygame.QUIT
                quit()

        if tmp > 1000 :
            c.moove([c.pos[0]-50, c.pos[1]+25])
            global ImageCar
            ImageCar = pygame.transform.rotate(ImageCar, 45)
            global car_rect
            car_rect = ImageCar.get_rect()
            car_rect.center = (c.pos[0],c.pos[1])
            tmp = 0
            

        surface.blit(background,(0,0))
        surface.blit(ImageCar,car_rect)
        pygame.display.update()


main()
