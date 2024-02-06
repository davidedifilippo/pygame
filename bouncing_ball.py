import sys
import pygame

pygame.init()

# screen size
width = 800
height = 600

# make screen
screen = pygame.display.set_mode((width, height))

# load ball image
ball = pygame.image.load("football.png")
x, y = ball.get_size()

print('width_Ball in pixel', x)
print('height_Ball in pixel', y)

# speed in pixel per frame
speed = [1, 1]
black = 100, 10, 0

# object too big
shrinkFactor = 0.2

ball = pygame.transform.scale(ball, (int(x * shrinkFactor), int(y * shrinkFactor)))
ball_rect = ball.get_rect()

# The clock provides several functions to help control a game's fps.
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()

    # By calling Clock.tick(150) once per frame, the program will never run at more than 150 frames per second.

    clock.tick(150)
    print(clock.get_fps())
