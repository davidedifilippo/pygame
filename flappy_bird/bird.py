import pygame.sprite


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0

        for i in range(3):
            img = pygame.image.load(f"img/bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.index += 1
        if self.index > 2:
            self.index = 0
        self.image = self.images[self.index]




