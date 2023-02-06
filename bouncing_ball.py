import sys, pygame
pygame.init()

size = width, height = 1000, 1200
speed = [2, 1]
black = 50, 10, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("football-gd5b0bcc66_640.png")
x, y = ball.get_size()
sf = 0.2


ball = pygame.transform.scale(ball, (int(x*sf), int(y*sf)))
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
