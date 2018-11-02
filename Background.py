import pygame

SCREEN_RECT = pygame.Rect(0, 0, 422, 950)


class Background(pygame.sprite.Sprite):

    def __init__(self, is_alt=False):

        super().__init__()

        self.image = pygame.image.load('./images/background.jpeg')

        self.rect = self.image.get_rect()

        self.speed = 1

        self.is_alt = is_alt

        if self.is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        self.rect.y += self.speed

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

    def set_position(self):

        self.rect = self.image.get_rect()

        if self.is_alt:
            self.rect.y = -self.rect.height


