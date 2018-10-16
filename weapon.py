import pygame
import Hero
from os import path
import weapon

longshot =[pygame.image.load("images/longshot/shot_1.png"),pygame.image.load("images/longshot/shot_2.png"),pygame.image.load("images/longshot/shot_3.png"),pygame.image.load("images/longshot/shot_4.png"),pygame.image.load("images/longshot/shot_5.png"),pygame.image.load("images/longshot/shot_6.png"),pygame.image.load("images/longshot/shot_7.png")]
bullet1 = [pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet2.png"),]
rocket = [pygame.image.load("images/rocket/shot_1.png"),pygame.image.load("images/rocket/shot_2.png"),pygame.image.load("images/rocket/shot_3.png"),pygame.image.load("images/rocket/shot_4.png"),pygame.image.load("images/rocket/shot_5.png"),pygame.image.load("images/rocket/shot_6.png"),pygame.image.load("images/rocket/shot_7.png")]
weapon_frequency = [500, 1000,60]


class Weapon(pygame.sprite.Sprite):
    animate = 1
    path = [0,animate**4]
    weapon_choice = 1
    weapon_img = [bullet1,rocket,longshot]
    weapon_speed = [-10, -5,0]
    animation_speed = [3, 15,-1]

    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = self.weapon_img[self.weapon_choice][0]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = self.weapon_speed[self.weapon_choice]
        self.frequency = weapon_frequency[self.weapon_choice]
        self.frequency_count = self.frequency
        self.WEAPON_CHOICE = self.weapon_choice;
        self.mask = pygame.mask.from_surface(self.image)
        # survival
        self.survival = True
    def check_animate(self):
            self.animate+=1
            if (len(self.weapon_img[self.WEAPON_CHOICE])*self.animation_speed[self.WEAPON_CHOICE] <= self.animate):
                self.animate = 0



    def change_img(self):
        self.image = self.weapon_img[self.WEAPON_CHOICE][self.animate//self.animation_speed[self.WEAPON_CHOICE]]
    def update(self):

        #if(self.WEAPON_CHOICE==2):
         #   self.image = pygame.transform.scale(,(90,90))

        self.check_animate()
        self.rect.y += self.weapon_speed[self.WEAPON_CHOICE]

        self.frequency_count -=1
        self.change_img()
        if self.rect.bottom<0:
            self.kill()










