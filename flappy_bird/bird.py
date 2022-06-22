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
        self.velocity = 0

    def update(self):
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.bottom < 768:
            self.rect.y += int(self.velocity)
        if pygame.mouse.get_pressed()[0] == 1:
            self.velocity = -10

        self.index += 1
        if self.index > 2:
            self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.images[self.index], -self.velocity * 2)


