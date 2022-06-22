import pygame
from bird import Bird
from pipe import Pipe
import random

clock = pygame.time.Clock()

fps = 60

pygame.init()

screen_width = 864
screen_height = 768 + 168
pipe_gap = 150
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks()
on_ground = True

scroll_ground = 0
scroll_speed = 4

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy bird")

bg = pygame.image.load("img/bg.png")
ground = pygame.image.load("img/ground.png")

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))
g_pipe = Pipe(400, int(screen_height / 2 + pipe_gap / 2), on_ground, scroll_speed)
c_pipe = Pipe(400, int(screen_height / 2 - pipe_gap / 2), not on_ground, scroll_speed)

bird_group.add(flappy)
pipe_group.add(g_pipe)
pipe_group.add(c_pipe)

run = True

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()

    now = pygame.time.get_ticks()
    if now - last_pipe > pipe_frequency:
        pipe_height = random.randint(100, 300)
        g_pipe = Pipe(screen_width, int(screen_height / 2 + pipe_height / 2), on_ground, scroll_speed)
        c_pipe = Pipe(screen_width, int(screen_height / 2 - pipe_height / 2), not on_ground, scroll_speed)
        pipe_group.add(g_pipe)
        pipe_group.add(c_pipe)
        last_pipe = pygame.time.get_ticks()
    pipe_group.draw(screen)
    pipe_group.update()
    screen.blit(ground, (scroll_ground, 768))
    scroll_ground -= scroll_speed

    if abs(scroll_ground) > 35:
        scroll_ground = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if flappy.rect.bottom > 768:
        run = False
    pygame.display.update()
pygame.quit()
