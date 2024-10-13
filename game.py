import pygame
import time
pygame.init()

WIDTH = 1000
HEIGHT = 799

screen = pygame.display.set_mode((WIDTH,HEIGHT))

banner = pygame.image.load("Lesson 3/images/birthdaybanner.jpg")
banner = pygame.transform.scale(banner,(WIDTH,HEIGHT))
cake = pygame.image.load("Lesson 3/images/cake.jpg")
cake = pygame.transform.scale(cake,(WIDTH,HEIGHT))
gift = pygame.image.load("Lesson 3/images/giftsopening.jpg")
gift = pygame.transform.scale(gift,(WIDTH,HEIGHT))

font = pygame.font.SysFont("Tristan",72)
text1 = font.render("Happy Birthday!",True,(227, 24, 9))
text2 = font.render("This is the cake, I hope you like it!",True,(227, 24, 9))
text3 = font.render("Come over here, I got you some gifts!",True,(227, 24, 9))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    screen.blit(banner,(0,0))
    screen.blit(text1,(300,200))
    pygame.display.update()
    time.sleep(4)
    screen.blit(cake,(0,0))
    screen.blit(text2,(100,90))
    pygame.display.update()
    time.sleep(4)
    screen.blit(gift,(0,0))
    screen.blit(text3,(80,100))
    pygame.display.update()
    time.sleep(4)
