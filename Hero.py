import pygame
from pygame.locals import *
import weapon


class Hero(pygame.sprite.Sprite):

    def __init__(self, background_size):
        super().__init__()

        '''
        This part need to be changed, basis on the # of pictures
        '''

        self.plane1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.plane2 = pygame.image.load("./images/me2.png").convert_alpha()
        # the output plane
        self.plane = self.plane1
        # set hero position
        self.background_rect = background_size
        self.rect = self.plane1.get_rect()
        self.set_position()
        # mask for collide check
        self.mask = pygame.mask.from_surface(self.plane)

        # set hero death animation list
        '''
        This part is not ready yet
        
        self.death_spirits = list()
        
        '''
        # set here death animation
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
        # bool variable for moving animation
        self.switch = True
        # counter for moving animation
        self.counter = 30
        # set hero speed
        self.speed = 5
        # survival
        self.survival = True

    def __move_up(self):
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def __move_down(self):
        if self.rect.bottom > self.background_rect.bottom:
            self.rect.bottom = self.background_rect.bottom
        else:
            self.rect.bottom += self.speed

    def __move_left(self):
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def __move_right(self):
        if self.rect.right > self.background_rect.right:
            self.rect.right = self.background_rect.right
        else:
            self.rect.right += self.speed

############################################################
    def newbullet(self):
        global newweapon
        newweapon = weapon.Weapon(self.rect.centerx, self.rect.top)

    global shootflag
    shootflag = True

    def shoot(self):
        global shootflag

        if (shootflag == True):
            self.newbullet()
            shootflag = False

        if (newweapon.freqency_count == 0):
            shootflag = True
            newweapon.freqency_count = newweapon.freqency
        sprites.add(newweapon)
        weapons.add(newweapon)
        sprites.update()
        newweapon.freqency_count -= 1

############################################################
    def hero_move(self):
        # get_input from keyboard
        key_pressed = pygame.key.get_pressed()
        #
        if key_pressed[K_UP]:
            self.__move_up()
        if key_pressed[K_DOWN]:
            self.__move_down()
        if key_pressed[K_LEFT]:
            self.__move_left()
        if key_pressed[K_RIGHT]:
            self.__move_right()
        if key_pressed[K_1]:
            weapon.Weapon.weapon_choice = 0
        if key_pressed[K_2]:
            weapon.Weapon.weapon_choice = 1
        # change plane photo
        if self.switch:
            self.plane = self.plane1
        else:
            self.plane = self.plane2
        # counter
        if self.counter == 0:
            self.switch = not self.switch
            self.counter = 3
        # 计数器计数
        self.counter -= 1


    def set_position(self):
        
        self.survival = True
        self.rect.centerx = self.background_rect.centerx
        self.rect.bottom = self.background_rect.bottom - 60



sprites = pygame.sprite.Group()
weapons = pygame.sprite.Group()
