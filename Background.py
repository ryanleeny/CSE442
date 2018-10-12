import pygame

SCREEN_RECT = pygame.Rect(0, 0, 422, 950)


class Background(pygame.sprite.Sprite):

    def __init__(self, is_alt=False):

        super().__init__()
        #set image 
        self.image = pygame.image.load('./images/background.jpeg')
        #rect image 
        self.rect = self.image.get_rect()
        #init moving speed
        self.speed = 1

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()
        #moving y and spped
        self.rect.y += self.speed
        #if player hit the top
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


