import pygame

SCREEN_RECT = pygame.Rect(0, 0, 422, 950)


class Background(pygame.sprite.Sprite):

    def __init__(self, is_alt=False):

        super().__init__()

        self.image = pygame.image.load('background.jpeg')

        self.rect = self.image.get_rect()

        self.speed = 2

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        self.rect.y += self.speed

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

