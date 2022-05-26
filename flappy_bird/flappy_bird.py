import pygame
from bird import Bird


clock = pygame.time.Clock()

fps = 60

pygame.init()

screen_width = 864
screen_height = 768 + 168

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy bird")

bg = pygame.image.load("img/bg.png")
ground = pygame.image.load("img/ground.png")

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height/2))
bird_group.add(flappy)

scroll_ground = 0
scroll_speed = 4

run = True

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground, (scroll_ground, 768))
    scroll_ground -= scroll_speed

    if abs(scroll_ground) > 35:
        scroll_ground = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
