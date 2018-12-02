import pygame
import random

CREATE_PAWN_EVENT = pygame.USEREVENT + 1

CREATE_OFFICER_EVENT = pygame.USEREVENT + 2

CREATE_MID_BOSS_EVEN = pygame.USEREVENT + 4


class Pawn(pygame.sprite.Sprite):

    def __init__(self, background_size, speed):
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
        self.speed = speed
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


class Officer(pygame.sprite.Sprite):

    hp = 5

    def __init__(self, background_size, speed):
        super().__init__()
        # get the image
        self.officer1 = pygame.image.load("./images/enemy2.png").convert_alpha()
        # output image
        self.officer = self.officer1
        # set hero position
        self.background_rect = background_size
        self.rect = self.officer1.get_rect()
        self.set_position()
        # mask for collide check
        self.mask = pygame.mask.from_surface(self.officer)
        # hit bool
        self.hit = False
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
        self.speed = speed
        # survival
        self.survival = True

    def move(self):
        self.rect.y += self.speed
        # if self.rect.y >= self.background_rect.height:
        #     self.kill()

    def set_position(self):
        self.survival = True
        self.rect.bottom = 0
        max_x = self.background_rect.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


class Mid_boss(pygame.sprite.Sprite):

    hp = 20

    def __init__(self, background_size, speed):
        super().__init__()
        # get the image
        self.mid_boss1 = pygame.image.load("./images/enemy3.png").convert_alpha()
        # output image
        self.mid_boss = self.mid_boss1
        # set hero position
        self.background_rect = background_size
        self.rect = self.mid_boss1.get_rect()
        self.set_position()
        # mask for collide check
        self.mask = pygame.mask.from_surface(self.mid_boss)
        # hit bool
        self.hit = False
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
        self.speed = speed
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


def add_enemies(name, bg_size, group1, group2, level):
    if name == 'pawn':
        if level <= 2:
            speed = random.randint(3, 6)
        elif 2 < level <= 4:
            speed = random.randint(5, 7)
        elif 4 < level <= 7:
            speed = random.randint(7, 9)
        elif 7 < level < 10:
            speed = random.randint(8, 11)
        else:
            speed = 15
        enemy = Pawn(bg_size, speed)
    if name == 'officer':
        if level <= 2:
            speed = random.randint(2, 4)
        elif 2 < level <= 4:
            speed = random.randint(4, 6)
        elif 4 < level <= 7:
            speed = random.randint(6, 7)
        elif 7 < level < 10:
            speed = random.randint(7, 8)
        else:
            speed = 9
        enemy = Officer(bg_size, speed)
    if name == 'mid_boss':
        if level <= 2:
            speed = random.randint(2, 3)
        elif 2 < level <= 4:
            speed = random.randint(3, 4)
        elif 4 < level <= 7:
            speed = random.randint(4, 5)
        elif 7 < level < 10:
            speed = random.randint(5, 6)
        else:
            speed = 8
        enemy = Mid_boss(bg_size, speed)

    group1.add(enemy)
    group2.add(enemy)


