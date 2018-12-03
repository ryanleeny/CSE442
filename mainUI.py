import pygame
import random
import Background as bg
import Hero
import Enemies
import weapon

TIMER = pygame.USEREVENT + 5

class Button(object):
    def button(text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        global setting_flag, gaming_flag, home_flag, fifteen_flag, thirty_flag, sixty_flag, game_over, refresh_flag, how_to_play_flag, pause_flag
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1 and action is not None:

                if action == "30":
                    fifteen_flag = True
                    thirty_flag = False
                    sixty_flag = False

                if action == "60":

                    fifteen_flag = False
                    thirty_flag = True
                    sixty_flag = False

                if action == "90":

                    fifteen_flag = False
                    thirty_flag = False
                    sixty_flag = True

                if action == "home":
                    gaming_flag = False
                    setting_flag = False
                    home_flag = True
                    game_over = False
                    refresh_flag = False
                    how_to_play_flag = False
                    pause_flag = False

                if action == "setting":
                    gaming_flag = False
                    setting_flag = True
                    home_flag = False
                    game_over = False
                    refresh_flag = False
                    how_to_play_flag = False
                    pause_flag = False

                if action == "play":
                    gaming_flag = True
                    setting_flag = False
                    home_flag = False
                    game_over = False
                    refresh_flag = False
                    how_to_play_flag = False
                    pause_flag = False

                if action == "how_to_play":
                    gaming_flag = False
                    setting_flag = False
                    home_flag = False
                    game_over = False
                    refresh_flag = False
                    how_to_play_flag = True
                    pause_flag = False

                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))
        Button.text_to_button(text, black, x, y, width, height)

    def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
        textSurf, textRect = Button.text_objects(msg, color, size)
        textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
        window.blit(textSurf, textRect)

    def text_objects(text, color, size="small"):
        smallfont = pygame.font.SysFont("comicsansms", 25)
        medfont = pygame.font.SysFont("comicsansms", 50)
        largefont = pygame.font.SysFont("comicsansms", 85)
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        if size == "medium":
            textSurface = medfont.render(text, True, color)
        if size == "large":
            textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()


class gameover(object):
    @staticmethod
    def finish():
        myfont = pygame.font.Font(None, 60)
        text = myfont.render("GAME OVER", True, red)
        window.blit(text, (80, 140))

        Button.button("Retry", 150, 300, 100, 50, gray, (163, 163, 163), action="play")
        Button.button("Exit", 150, 450, 100, 50, gray, (163, 163, 163), action="home")


class gamepause(object):
    @staticmethod
    def pause():
        myfont = pygame.font.Font(None, 60)
        text = myfont.render("Pause", True, red)
        window.blit(text, (140, 140))

        Button.button("Retry", 150, 350, 100, 50, gold, (255, 255, 255), action="play")
        Button.button("Continue", 150, 250, 100, 50, gold, (255, 255, 255))
        Button.button("Exit", 150, 450, 100, 50, gold, (255, 255, 255), action="home")


class Setting(object):
    @staticmethod
    def option():
        pygame.draw.line(window, white, (80, 300), (320, 300), 3)  # Draw a line
        window.blit(voice_col, (z, 289))
        window.blit(voice_low, (40, 277))
        window.blit(voice_high, (320, 277))

        myfont2 = pygame.font.Font(None, 30)
        text2 = myfont2.render(str(z4), True, black)
        window.blit(text2, (z, 270))

        window.blit(fps, (55, 380))

        Button.button("slow", 190, 380, 100, 50, col1, (255, 255, 255), action="30")
        Button.button("medium", 190, 450, 100, 50, col2, (255, 255, 255), action="60")
        Button.button("fast", 190, 520, 100, 50, col3, (255, 255, 255), action="90")
        window.blit(home, (350, 652))

class howToPlay(object):
    @staticmethod
    def option():
        window.blit(home, (350, 652))


class main(object):
    ####global functions here#####
    global text_objects, galaxy_background
    global window

    #####global varaible declaration here#####
    global black, white, green, red, gold, blue, yellow,gray, game_record, home, background, background2, background3, background5, fps, voice_col,\
        voice_low, voice_high, sound_off, width, height, x, y, cursor1, home_flag, gaming_flag, setting_flag, sound_on, \
        background4, game_over, refresh_flag, highest_score, pause_flag
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (34, 177, 76)
    yellow = (200, 200, 0)
    red = (200, 0, 0)
    gold = (227, 207, 87)
    blue = (23, 44, 225)
    gray = (46,46,46)
    width = 401  # Window width
    height = 700  # Window height
    SCREEN_RECT = pygame.Rect(0, 0, width, height)
    game_record = 0  # score to display in the screen
    background = pygame.image.load('./images/background.jpeg')
    background2 = pygame.image.load('./images/bg2.jpeg')
    background3 = pygame.image.load('./images/bg3.jpg')
    background4 = pygame.image.load('./images/bg4.jpg')
    background5 =  pygame.image.load('./images/bg5.jpg')
    cursor1 = pygame.image.load('./images/ship.png')  # vhighest_scoreery basic design on the cursor/ship, but can work on it later
    voice_low = pygame.image.load('./images/vl.png')
    voice_high = pygame.image.load('./images/vh.png')
    voice_col = pygame.image.load('./images/vc.png')
    sound_off = pygame.image.load('./images/so.png')
    sound_on = pygame.image.load('./images/sb.png')
    home = pygame.image.load('./images/home.png')
    fps = pygame.image.load('./images/fps.png')
    game_over = False
    gaming_flag = False
    setting_flag = False
    home_flag = True
    refresh_flag = False
    how_to_play_flag = False
    pause_flag = False

    global pawn_score, officer_score, mid_boss_score
    pawn_score = 10
    officer_score = 50
    mid_boss_score = 100

    ####Unuse Declaration#####
    x = width * 1  # x and y is the position of background img
    y = height * 1

    #####The font of button object#####
    def text_objects(text, font):
        textSurface = font.render(text, True, gold)
        return textSurface, textSurface.get_rect()

    def __create_sprites_group(self):
        bg1 = bg.Background()
        bg2 = bg.Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.hero = Hero.Hero(self.SCREEN_RECT)
        self.enemies = pygame.sprite.Group()
        self.pawn_enemies = pygame.sprite.Group()
        self.office_enemies = pygame.sprite.Group()
        self.mid_boss_enemies = pygame.sprite.Group()

    def __update_score(self):

        score_text = self.Score_text.render("Score : %s" % str(self.game_score), True, yellow)
        window.blit(score_text, (10, 5))

    def __display_level(self):

        level_text = self.Score_text.render("Lv : %s" % str(self.level), True, yellow)
        window.blit(level_text, (300, 5))

    def __update_sprites(self):
        # move background
        self.bg_group.update()
        self.bg_group.draw(window)

        # move hero
        if self.hero.survival:
            self.hero.hero_move()
            window.blit(self.hero.plane, self.hero.rect)
        else:
            global game_over, gaming_flag, refresh_flag, highest_score

            gaming_flag = False
            game_over = True
            refresh_flag = True

            if self.game_score > highest_score:
                with open("score.txt", "w") as f:
                    f.write(str(self.game_score))
                    f.close()
                    highest_score = self.game_score

        for bullet in self.hero.weapons:
            if bullet.survival:
                bullet.update()
                window.blit(bullet.image, bullet.rect)
            else:
                bullet.kill()

        # move pawn enemies
        for pawn in self.pawn_enemies:
            if pawn.survival:
                pawn.move()
                window.blit(pawn.pawn, pawn.rect)
            else:
                self.game_score += pawn_score
                pawn.kill()

        for officer in self.office_enemies:
            if officer.survival:
                officer.move()
                if officer.rect.y >= self.SCREEN_RECT.height:
                    for ii in range(10):
                        Enemies.add_enemies("pawn", self.SCREEN_RECT, self.pawn_enemies, self.enemies, self.level)
                    officer.kill()
                if officer.hit:
                    pass
                else:
                    window.blit(officer.officer, officer.rect)
                # get the blood bar
                draw_bar_start = (officer.rect.left, officer.rect.top - 5)
                draw_bar_end = (officer.rect.right, officer.rect.top - 5)
                pygame.draw.line(window, (255, 0, 0), draw_bar_start, draw_bar_end, 2)
                # get the actual
                actual_blood = officer.hp / Enemies.Officer.hp
                draw_bar_end = (officer.rect.left + officer.rect.width * actual_blood, officer.rect.top - 5)
                pygame.draw.line(window, (0, 255, 0), draw_bar_start, draw_bar_end, 2)
            else:
                self.game_score += officer_score
                officer.kill()
        
        for mid_boss in self.mid_boss_enemies:

            if mid_boss.survival:
                mid_boss.move()
                if mid_boss.hit:
                    pass
                else:
                    window.blit(mid_boss.mid_boss, mid_boss.rect)
                # get the blood bar
                draw_bar_start = (mid_boss.rect.left, mid_boss.rect.top - 5)
                draw_bar_end = (mid_boss.rect.right, mid_boss.rect.top - 5)
                pygame.draw.line(window, (255, 0, 0), draw_bar_start, draw_bar_end, 2)
                # get the actual
                actual_blood = mid_boss.hp / Enemies.Mid_boss.hp
                draw_bar_end = (mid_boss.rect.left + mid_boss.rect.width * actual_blood, mid_boss.rect.top - 5)
                pygame.draw.line(window, (0, 255, 0), draw_bar_start, draw_bar_end, 2)
            else:
                self.game_score += mid_boss_score
                mid_boss.kill()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif gaming_flag:
                if event.type == Enemies.CREATE_PAWN_EVENT:
                    Enemies.add_enemies("pawn", self.SCREEN_RECT, self.pawn_enemies, self.enemies, self.level)
                elif event.type == Enemies.CREATE_OFFICER_EVENT:
                    Enemies.add_enemies("officer", self.SCREEN_RECT, self.office_enemies, self.enemies, self.level)
                elif event.type == Enemies.CREATE_MID_BOSS_EVEN:
                    Enemies.add_enemies("mid_boss", self.SCREEN_RECT, self.mid_boss_enemies, self.enemies, self.level)
                elif event.type == Hero.HERO_SHOOT_EVENT:
                    self.hero.shoot()
                    if weapon.Weapon.weapon_choice == 1:
                        self.game_score -= 5

                    if weapon.Weapon.weapon_choice == 2 and weapon.minus_score:
                        self.game_score -= 50
                    weapon.minus_score = False

            elif event.type == TIMER:
                self.__set_time()

    def __check_collide(self):
        enemies_down = pygame.sprite.spritecollide(self.hero, self.enemies, False, pygame.sprite.collide_mask)

        if enemies_down:
            self.hero.survival = False
            for enemy in enemies_down:
                enemy.survival = False

        for bullet in self.hero.weapons:
            enemy_hit = pygame.sprite.spritecollide(bullet, self.enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                if weapon.Weapon.weapon_choice != 2:
                    bullet.survival = False

                for enemy in enemy_hit:
                    if enemy in self.office_enemies:
                        if weapon.Weapon.weapon_choice == 1:
                            enemy.hp -= 2
                        else:
                            enemy.hp -= 1
                        if enemy.hp == 0 or enemy.hp < 0:
                            enemy.survival = False

                    if enemy in self.pawn_enemies:
                        enemy.survival = False

                    if enemy in self.mid_boss_enemies:
                        if weapon.Weapon.weapon_choice == 1:
                            enemy.hp -= 2
                        else:
                            enemy.hp -= 1
                        if enemy.hp == 0 or enemy.hp < 0:
                            enemy.survival = False

    def __refresh_game(self):

        # kill all elements for gaming
        self.pawn_enemies.empty()
        self.office_enemies.empty()
        self.mid_boss_enemies.empty()
        self.enemies.empty()
        self.hero.weapons.empty()

        # reset game
        self.hero.set_position()
        self.game_score = 0
        self.level = 1

        # reset weapon
        weapon.Weapon.weapon_choice = 0

        # reset bg position
        for back_g in self.bg_group:

            back_g.set_position()

        # reset timer
        # default create pawn enemy time 1000ms
        # create_pawn_time = 1000
        # # default create office enemy time 5000ms
        # create_office_time = 5000
        # # default create office enemy time 5000ms
        # create_mid_boss_time = 10000
        # # reset create pawn timer
        # pygame.time.set_timer(Enemies.CREATE_PAWN_EVENT, create_pawn_time)
        # # reset create officer timer
        # pygame.time.set_timer(Enemies.CREATE_OFFICER_EVENT, create_office_time)
        # # reset create officer timer
        # pygame.time.set_timer(Enemies.CREATE_MID_BOSS_EVEN, create_mid_boss_time)
        self.__set_time()

    def __set_time(self):

        if self.level < 3:
            # default create pawn enemy time 1000ms, will change during the score up
            create_pawn_time = random.randint(800 - ((self.level - 1) * 50), 1200 - ((self.level - 1) * 50))
            # default create office enemy time 5000ms, will change during the score up
            create_office_time = random.randint(2500 - ((self.level - 1) * 50), 3000 - ((self.level - 1) * 50))
            # default create office enemy time 5000ms, will change during the score up
            create_mid_boss_time = random.randint(10000 - ((self.level - 1) * 50), 12000 - ((self.level - 1) * 50))
        elif 3 <= self.level < 5:
            # default create pawn enemy time 1000ms, will change during the score up
            create_pawn_time = random.randint(700 - ((self.level - 2) * 100), 1100 - ((self.level - 2) * 100))
            # default create office enemy time 5000ms, will change during the score up
            create_office_time = random.randint(2000 - ((self.level - 2) * 100), 2500 - ((self.level - 2) * 100))
            # default create office enemy time 5000ms, will change during the score up
            create_mid_boss_time = random.randint(7000 - ((self.level - 2) * 100), 9000 - ((self.level - 2) * 100))
        elif 5 <= self.level < 8:
            # default create pawn enemy time 1000ms, will change during the score up
            create_pawn_time = random.randint(500 - ((self.level - 5) * 50), 1200 - ((self.level - 5) * 50))
            # default create office enemy time 5000ms, will change during the score up
            create_office_time = random.randint(1750 - ((self.level - 5) * 150), 2750 - ((self.level - 5) * 150))
            # default create office enemy time 5000ms, will change during the score up
            create_mid_boss_time = random.randint(5000 - ((self.level - 5) * 150), 6000 - ((self.level - 5) * 150))
        elif 8 <= self.level:
            # default create pawn enemy time 1000ms, will change during the score up
            create_pawn_time = random.randint(350, 1150 - ((self.level - 8) * 50))
            # default create office enemy time 5000ms, will change during the score up
            create_office_time = random.randint(1000, 3000 - ((self.level - 8) * 50))
            # default create office enemy time 5000ms, will change during the score up
            create_mid_boss_time = random.randint(3000, 4500 - ((self.level - 8) * 50))

        pygame.time.set_timer(Enemies.CREATE_PAWN_EVENT, create_pawn_time)
        # set create officer timer
        pygame.time.set_timer(Enemies.CREATE_OFFICER_EVENT, create_office_time)
        # set create officer timer
        pygame.time.set_timer(Enemies.CREATE_MID_BOSS_EVEN, create_mid_boss_time)

    def __score(self):

        if self.game_score < 0:
            global game_over, gaming_flag, refresh_flag, highest_score

            gaming_flag = False
            game_over = True
            refresh_flag = True

    def __level(self):
        level = 0
        if self.game_score < 100:
            level = 1
        elif 100 <= self.game_score < 200:
            level = 2
        elif 200 <= self.game_score < 500:
            level = 3
        elif 500 <= self.game_score < 600:
            level = 4
        elif 600 <= self.game_score < 1000:
            level = 5
        elif 1000 <= self.game_score < 2000:
            level = 6
        elif 2000 <= self.game_score < 3000:
            level = 7
        elif 3000 <= self.game_score < 4000:
            level = 8
        elif 5000 <= self.game_score < 6000:
            level = 9
        elif 6000 <= self.game_score < 7000:
            level = 10

        if self.level < level:
            self.level = level

        self.hero.speed = 5 + ((self.level - 1) * 0.5)


    ####Below initialize the GUI (Before LOOP)#####
    def __init__(self):
        global z, FPS, z2, z3, z4, z5, i, j, k, m, col1, col2, col3, highest_score
        i = 1
        j = 1
        k = 1
        m = 1
        z = 180
        z2 = z
        z5 = (z - 80) / 220
        z3 = z5 * 100
        z4 = int(z3)
        FPS = 60

        col1 = col3 = gold
        col2 = white

        # default create pawn enemy time 1000ms, will change during the score up
        create_pawn_time = 1000
        # default create office enemy time 5000ms, will change during the score up
        create_office_time = 5000
        # default create office enemy time 5000ms, will change during the score up
        create_mid_boss_time = 10000

        # hero shoot time
        hero_shoot_fre = weapon.weapon_frequency[weapon.Weapon.weapon_choice]
        # init sprites_group
        self.__create_sprites_group()
        # # set create pawn timer
        # pygame.time.set_timer(Enemies.CREATE_PAWN_EVENT, create_pawn_time)
        # # set create officer timer
        # pygame.time.set_timer(Enemies.CREATE_OFFICER_EVENT, create_office_time)
        # # set create officer timer
        # pygame.time.set_timer(Enemies.CREATE_MID_BOSS_EVEN, create_mid_boss_time)
        # set shoot timer
        pygame.time.set_timer(Hero.HERO_SHOOT_EVENT, hero_shoot_fre)
        # emeny refresh rate set
        pygame.time.set_timer(TIMER, 500)
        # get highest score
        with open("./score.txt", 'r') as f:
            highest_score = int(f.read())
            f.close()

        ####Play background music####
        pygame.mixer.music.load('music/Tech Inc1 Loop.wav')  # load the music
        pygame.mixer.music.play(-1)  # -1 means unlimit play
        # pygame.mixer.music.queue('next.mp3') #second music
        pygame.mixer.music.set_volume(z5)
        # creating font object
        self.Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)
        # in game score
        self.game_score = 0
        # in game level
        self.level = 1


        # ###main loop of the GUI#### #
        game_loop = True  # ;This the the loop of the main game, FALSE to exit the loop
        while game_loop:
            self.__event_handler()


            # init sprites_group
            # ####Add Keyboard press detection##### #
            k_press = pygame.key.get_pressed()
            # ####Add Mouse press detection and get position of mouse##### #
            mouse_press = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            # ####add backcground moving alone with mouse#### #

            global x, y, fifteen_flag, thirty_flag, sixty_flag, retry_flag, gaming_flag, setting_flag, home_flag, pause_flag, how_to_play_fla

            x = mouse[0] * -0.05
            y = mouse[1] * -0.05
            fifteen_flag = False #fps#
            thirty_flag = False
            sixty_flag = False

            # ####mouse##### #
            mx = mouse[0] - cursor1.get_width() / 2
            my = mouse[1] - cursor1.get_height() / 2
            pygame.mouse.set_visible(False)

            if gaming_flag:

                # load the background music for game
                if i == 1:
                    j = k
                    pygame.mixer.music.load('music/Defense Line.mp3')
                    pygame.mixer.music.play(-1)
                    i = 2

                # pause game
                if (k_press[pygame.K_ESCAPE] == True):
                    i = 3
                    pygame.mixer.music.pause()
                if i == 3:
                    gaming_flag = False
                    pause_flag = True

                # game running
                if i == 2:
                    # check collision
                    self.__check_collide()
                    # function for update screen
                    self.__update_sprites()
                # function for update score display

                self.__update_score()
                # update level
                self.__level()
                # display level
                self.__display_level()
                # check if score is less than 0
                self.__score()


            elif pause_flag:
                window.blit(background4, (x, y))
                gamepause.pause()
                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

                if (248 >= mouse[0] >= 147) and (262 <= mouse[1] <= 312) and (mouse_press[0] == True):

                    if k == 1:
                        pygame.mixer.music.unpause()
                    i = 2
                    pause_flag = False
                    gaming_flag = True

                elif (mouse_press[0] == True) and (248 >= mouse[0] >= 147) and (363 <= mouse[1] <= 412):
                    if k == 1:
                        i = 1
                    else:
                        i = 2
                    self.__refresh_game()
                    pause_flag = False
                    gaming_flag = True

                elif (248 >= mouse[0] >= 147) and (436 <= mouse[1] <= 512) and (mouse_press[0] == True):
                    pygame.mixer.music.load('music/Tech Inc1 Loop.wav')
                    pygame.mixer.music.play(-1)
                    if k == 2:
                        pygame.mixer.music.pause()
                    self.__refresh_game()
                    pause_flag = False
                    gaming_flag = False
                    home_flag = True


            elif game_over:
                i = k
                # background music back to main music
                if j == 1:
                    pygame.mixer.music.load('music/Tech Inc1 Loop.wav')
                    pygame.mixer.music.play(-1)
                    j = 3

                if j == 2:
                    pygame.mixer.music.load('music/Tech Inc1 Loop.wav')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.pause()
                    j = 3

                window.blit(background4, (x, y))
                gameover.finish()

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

                global refresh_flag

                if refresh_flag:
                    refresh_flag = False
                    self.__refresh_game()

            elif setting_flag:
                window.blit(background3, (x, y)) #set up the background
                Setting.option()  #branch to function named option() from class setting
                pygame.mixer.music.unpause()

                ###---volume control---###
                if z <= 80:
                    z = 80
                if z >= 300:
                    z = 300
                if (77 >= mouse[0] >= 48) and (300 <= mouse[1] <= 328) and (z > 80) and (mouse_press[0] == True):
                    z = z - 1
                    k = 1
                    z2 = z
                if (360 >= mouse[0] >= 320) and (296 <= mouse[1] <= 330) and (z < 300) and (mouse_press[0] == True):
                    z = z + 1
                    k = 1
                    z2 = z
                if (330 >= mouse[1] >= 295) and (310 >= mouse[0] >= 90) and (mouse_press[0] == True):
                    z = mouse[0] - 10
                    k = 1
                    z2 = z
                if (375 >= mouse[0] >= 347) and (662 <= mouse[1] <= 692) and (mouse_press[0] == True):
                    home_flag = True
                    setting_flag = False
                z5 = (z - 80) / 220
                pygame.mixer.music.set_volume(z5)
                z3 = z5 * 100
                z4 = int(z3)

                ###pfs###
                if fifteen_flag:
                    FPS = 30
                    col1 = white
                    col2 = col3 = gold
                    fifteen_flag = False
                    continue
                if thirty_flag:
                    FPS = 60
                    col2 = white
                    col1 = col3 = gold
                    thirty_flag = False
                    continue
                if sixty_flag:
                    FPS = 90
                    col3 = white
                    col2 = col1 = gold
                    sixty_flag = False
                    continue

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

            elif home_flag:
                window.blit(background3, (x, y))

                ####Create Button####
                Button.button("play", 150, 300, 100, 50, gray, (163, 163, 163), action="play")
                Button.button("setting", 150, 400, 100, 50, gray, (163, 163, 163), action="setting")
                Button.button("How To Play", 150, 500, 100, 50, gray, (163, 163, 163), action="how_to_play")
                Button.button("quit", 150, 600, 100, 50, gray, (163, 163, 163), action="quit")
                window.blit(sound_off, (0, 0))
                window.blit(sound_on, (50, 0))
                pygame.draw.line(window, black, (46, 6), (46, 42), 2)

                ####Mute button####
                i = j = k
                if m == 1:
                    z2 = z
                    m = 2
                if (42 >= mouse[0] >= 0) and (18 <= mouse[1] <= 55) and (mouse_press[0] == True):
                    pygame.mixer.music.pause()
                    i = 2
                    j = 2
                    k = 2
                    z = 80
                if (89 >= mouse[0] >= 46) and (18 <= mouse[1] <= 55) and (mouse_press[0] == True):
                    pygame.mixer.music.unpause()
                    m = 1
                    if k == 2:
                        z5 = (z2 - 80) / 220
                    pygame.mixer.music.set_volume(z5)
                    i = 1
                    j = 1
                    k = 1
                    z = z2

                ####coins_Display#####
                # Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)  # creating font object
                textSurf, Score = text_objects("Highest Score: %d" % highest_score, self.Score_text)  # Using the font object
                Score.center = (200, 140)  # location of font object
                window.blit(textSurf, Score)  # putting the font object in Window panel

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

            elif how_to_play_flag:
                window.blit(background5, (x, y))
                howToPlay.option()
                if (375 >= mouse[0] >= 347) and (662 <= mouse[1] <= 692) and (mouse_press[0] == True):
                    home_flag = True
                    how_to_play_fla = False
                window.blit(cursor1, (mx, my))


            #####refresh everything#####
            clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    game = main()
