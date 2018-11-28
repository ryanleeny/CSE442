import pygame
import Hero
from os import path
import weapon
import random
import mainUI

# load the bullets image into array
longshot =[pygame.image.load("images/longshot/shot_1.png"),pygame.image.load("images/longshot/shot_2.png"),pygame.image.load("images/longshot/shot_3.png"),pygame.image.load("images/longshot/shot_4.png"),pygame.image.load("images/longshot/shot_5.png"),pygame.image.load("images/longshot/shot_6.png"),]
bullet1 = [pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet1.png"),pygame.image.load("images/bullet2.png"),pygame.image.load("images/bullet1.png")]
rocket = [pygame.image.load("images/rocket/shot_1.png"),pygame.image.load("images/rocket/shot_2.png"),pygame.image.load("images/rocket/shot_3.png"),pygame.image.load("images/rocket/shot_4.png"),pygame.image.load("images/rocket/shot_5.png"),pygame.image.load("images/rocket/shot_6.png"),pygame.image.load("images/rocket/shot_7.png")]
weapon_frequency = [500, 200, 3000]  #set how fast the bullet come out of the player in ms
weapon_switched = False
pygame.init()
fire_sound = pygame.mixer.Sound("music/fire.wav")
bullet_sound =pygame.mixer.Sound("music/Blaster-Ricochet.wav")
laser_sound =pygame.mixer.Sound("music/blade2.wav")
weapon_sound = [bullet_sound,fire_sound,laser_sound]
minus_score = False

#initialzation of bullets
class Weapon(pygame.sprite.Sprite):
    animate = 1   # begining index of the array
    path = [0,animate**4]  #not use
    weapon_choice = 0   # which weapon are choosen, index of the weapons array
    weapon_img = [bullet1,rocket,longshot,] #weapons array
    weapon_speed = [-10, -5,0] #how fast the bullets are moving, the entry index are associated to the same index of the weapons array
    animation_speed = [3, 15,15] # how much pixls the bullets move up every refresh, here the bigger negative the faster bullets move
    weapon_timer = pygame.USEREVENT + 3
    weapon_timer_choice = [0, 120, 200]
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = self.weapon_img[self.weapon_choice][0]
        self.rect = self.image.get_rect()
        self.rect.bottom = y - 15
        self.rect.centerx = x
        self.speedy = self.weapon_speed[self.weapon_choice]
        self.frequency = weapon_frequency[self.weapon_choice]
        self.frequency_count = self.frequency
        self.WEAPON_CHOICE = self.weapon_choice
        self.mask = pygame.mask.from_surface(self.image)

        self.image = pygame.Surface(self.image.get_size()).convert_alpha(self.image)
        self.image = pygame.Surface((100, 100))
        # survival
        self.survival = True
        self.fire = False
        pygame.time.set_timer(self.weapon_timer, self.weapon_timer_choice[self.weapon_choice])
        pygame.mixer.Sound.play(weapon_sound[self.weapon_choice])

     #this update the index in the weapon image array, but with modification of incrementing speed
    def check_animate(self):
            self.animate+=1
            if (len(self.weapon_img[self.WEAPON_CHOICE])*self.animation_speed[self.WEAPON_CHOICE] <= self.animate):
                self.animate = 0


     #update the next image display of the weapon array, the index are pointed by the variable self.animate above
    def change_img(self):
        self.image = self.weapon_img[self.WEAPON_CHOICE][self.animate//self.animation_speed[self.WEAPON_CHOICE]]
        self.mask = pygame.mask.from_surface(self.image)
    #update the bullets class
    #special case
    def update(self):
        global minus_score
        # if(weapon_switched==True):
        #     clear_bullet(self)

        #nomral case
        self.check_animate()
        self.rect.y += self.weapon_speed[self.WEAPON_CHOICE]
        self.frequency_count -=1
        self.change_img()
        if self.rect.bottom < 0:
            self.kill()


        #longshot case
        if self.WEAPON_CHOICE == 2:

            rannum = random.randrange(-2, 3)
            self.rect.centerx += rannum
            if pygame.event.get(self.weapon_timer):
                self.fire = True
                minus_score = True
            if self.fire == True:
                self.rect.y += -10
                self.image = self.image = pygame.image.load("images/longshot/shot_7.png")
                self.mask = pygame.mask.from_surface(self.image)




        if self.WEAPON_CHOICE == 1:
            if pygame.event.get(self.weapon_timer):
                self.kill()


