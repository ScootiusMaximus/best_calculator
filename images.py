import pygame
import random
pygame.init()

size = 120


advert1 = pygame.transform.scale(pygame.image.load("images/advert1.jpg"),(500,size))
advert2 = pygame.transform.scale(pygame.image.load("images/advert2.jpg"),(500,size))
advert3 = pygame.transform.scale(pygame.image.load("images/advert3.jpg"),(500,size))
advert4 = pygame.transform.scale(pygame.image.load("images/advert4.jpg"),(500,size))
advert5 = pygame.transform.scale(pygame.image.load("images/advert5.jpg"),(500,size))
advert6 = pygame.transform.scale(pygame.image.load("images/advert6.jpg"),(500,size))
advert7 = pygame.transform.scale(pygame.image.load("images/advert7.jpg"),(500,size))
lock = pygame.image.load("images/lock.png")

ads = [advert1,advert2,advert3,advert4,advert5,advert6,advert7]
random.shuffle(ads)