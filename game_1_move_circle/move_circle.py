import pygame

game_window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Move circle")

# center

x = 600
y = 300

# radius

r = 20

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_window.fill((0, 0, 0))

    KeyPressed = pygame.key.get_pressed()
    # muovo di un pixel
    if KeyPressed[pygame.K_UP]:
        y -= 1
    if KeyPressed[pygame.K_DOWN]:
        y += 1
    if KeyPressed[pygame.K_LEFT]:
        x -= 1
    if KeyPressed[pygame.K_RIGHT]:
        x += 1

    pygame.draw.circle(game_window, (255, 90, 0), (x, y), r)
    pygame.display.update()
