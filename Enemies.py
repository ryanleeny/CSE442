import pygame
import random

CREATE_PAWN_EVENT = pygame.USEREVENT


class Pawn(pygame.sprite.Sprite):

    def __init__(self, background_size):
        super().__init__()
        # get the image
        self.pawn1 = pygame.image.load("./images/enemy1.png").convert_alpha()
        # output image
        self.pawn = self.pawn1
        # set hero position
        self.background_rect = background_size
        self.rect = self.pawn1.get_rect()
        self.set_position()
        # mask for collide check
        self.mask = pygame.mask.from_surface(self.pawn)
        '''
        This part is not ready yet

        self.death_spirits = list()

        '''
        # set pawn death animation
        '''
        This part need to be changed, basis on the # of pictures

        self.spirit1 = pygame.image.load('address').convert_alpha()
        self.spirit2 = pygame.image.load('address').convert_alpha()
        self.spirit3 = pygame.image.load('address').convert_alpha()
        '''

        '''    
        # put death animation in death animation list  
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3])
        '''
        # speed
        self.speed = 2
        # survival
        self.survival = True

    def move(self):
        self.rect.y += self.speed
        if self.rect.y >= self.background_rect.height:
            self.kill()

    def set_position(self):
        self.survival = True
        self.rect.bottom = 0
        max_x = self.background_rect.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


def add_enemies(name, bg_size, group1, group2):
    if name == 'pawn':
        enemy = Pawn(bg_size)

    group1.add(enemy)
    group2.add(enemy)