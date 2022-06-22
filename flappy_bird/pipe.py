import pygame.sprite


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, ground, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()
        self.ss = scroll_speed
        if ground:
            self.rect.topleft = [x, y]
        else:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]

    def update(self):
        self.rect.x -= self.ss
