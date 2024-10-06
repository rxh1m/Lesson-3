import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

banner = pygame.image.load("Lesson 3/images/birthdaybanner.jpg")
banner = pygame.transform.scale(banner,(600,900))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    screen.blit(banner,(0,0))
    pygame.display.update()
