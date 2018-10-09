import pygame
import tkinter.messagebox
import Background as bg
import Hero
import Enemies


class Button(object):
    def button(text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        global setting_flag, gaming_flag, home_flag, fifteen_flag, thirty_flag, sixty_flag
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1 and action is not None:

                if action == "15":
                    fifteen_flag = True
                    thirty_flag = False
                    sixty_flag = False

                if action == "30":

                    fifteen_flag = False
                    thirty_flag = True
                    sixty_flag = False

                if action == "60":

                    fifteen_flag = False
                    thirty_flag = False
                    sixty_flag = True

                if action == "home":
                    gaming_flag = False
                    setting_flag = False
                    home_flag = True

                if action == "setting":
                    #print("Setting Button Clicked")
                    gaming_flag = False
                    setting_flag = True
                    home_flag = False

                if action == "play":
                    #print("Play Button Click, go to gameLoop")
                    gaming_flag = True
                    setting_flag = False
                    home_flag = False

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


class Setting(object):
    @staticmethod
    def option():
        pygame.draw.line(window, white, (80, 300), (320, 300), 3)  # Draw a line
        window.blit(voice_col, (z, 289))
        window.blit(voice_low, (40, 277))
        window.blit(voice_high, (320, 277))
        window.blit(fps, (55, 380))
        Button.button("15", 190, 380, 100, 50, gold, (255, 255, 255), action="15")
        Button.button("30", 190, 450, 100, 50, gold, (255, 255, 255), action="30")
        Button.button("60", 190, 520, 100, 50, gold, (255, 255, 255), action="60")
        Button.button("", 336, 638, 50, 50, white, (255, 255, 255), action="home")
        window.blit(home, (350, 652))


class main(object):
    ####global functions here#####
    global text_objects, galaxy_background
    global window

    #####global varaible declaration here#####
    global black, white, green, red, gold, blue, yellow, game_score, home, background, background2, background3, fps, voice_col,\
        voice_low, voice_high, sound_off, width, height, x, y, cursor1, home_flag, gaming_flag, setting_flag, sound_on
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (34, 177, 76)
    yellow = (200, 200, 0)
    red = (200, 0, 0)
    gold = (227, 207, 87)
    blue = (23, 44, 225)
    width = 401  # Window width
    height = 700  # Window height
    SCREEN_RECT = pygame.Rect(0, 0, width, height)
    game_score = 0  # score to display in the screen
    background = pygame.image.load('./images/background.jpeg')
    background2 = pygame.image.load('./images/bg2.jpeg')
    background3 = pygame.image.load('./images/bg3.jpg')
    cursor1 = pygame.image.load('./images/ship.png')  # very basic design on the cursor/ship, but can work on it later
    voice_low = pygame.image.load('./images/vl.png')
    voice_high = pygame.image.load('./images/vh.png')
    voice_col = pygame.image.load('./images/vc.png')
    sound_off = pygame.image.load('./images/so.png')
    sound_on = pygame.image.load('./images/sb.png')
    home = pygame.image.load('./images/home.png')
    fps = pygame.image.load('./images/fps.png')
    gaming_flag = False
    setting_flag = False
    home_flag = True

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

    def __update_sprites(self):
        # move background
        self.bg_group.update()
        self.bg_group.draw(window)
        # move hero
        if self.hero.survival:
            self.hero.hero_move()
            window.blit(self.hero.plane, self.hero.rect)
        # move pawn enemies
        for pawn in self.pawn_enemies:
            if pawn.survival:
                pawn.move()
                window.blit(pawn.pawn, pawn.rect)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif gaming_flag:
                if event.type == Enemies.CREATE_PAWN_EVENT:
                    Enemies.add_enemies("pawn", self.SCREEN_RECT, self.pawn_enemies, self.enemies)

    ####Below initialize the GUI (Before LOOP)#####
    def __init__(self):
        global z, FPS, z2
        z = 180
        z2 = z
        FPS = 60
        # default create pawn enemy time 1500ms, will change during the score up
        create_pawn_time = 1500
        self.__create_sprites_group()
        # set create pawn timer
        pygame.time.set_timer(Enemies.CREATE_PAWN_EVENT, create_pawn_time)

        ####Play background music####
        pygame.mixer.music.load('music/Power Bots Loop.wav')  # load the music
        pygame.mixer.music.play(-1)  # -1 means unlimit play
        # pygame.mixer.music.queue('next.mp3') #second music
        pygame.mixer.music.set_volume((z - 80) / 220)

        # ###main loop of the GUI#### #
        game_loop = True  # ;This the the loop of the main game, FALSE to exit the loop
        while game_loop:
            self.__event_handler()

            # ####Add Keyboard press detection##### #
            k_press = pygame.key.get_pressed()
            # ####Add Mouse press detection and get position of mouse##### #
            mouse_press = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            # ####add backcground moving alone with mouse#### #
            global x, y, fifteen_flag, thirty_flag, sixty_flag
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
                # function for update screen
                pygame.mixer.music.stop()
                self.__update_sprites()

            elif setting_flag:
                window.blit(background2, (x, y)) #set up the background
                Setting.option()  #branch to function named option() from class setting
                pygame.mixer.music.unpause()

                ###---volume control---###
                if z <= 80:
                    z = 80
                if z >= 300:
                    z = 300
                if (77 >= mouse[0] >= 48) and (300 <= mouse[1] <= 328) and (z > 80) and (mouse_press[0] == True):
                    z = z - 10
                if (360 >= mouse[0] >= 320) and (296 <= mouse[1] <= 330) and (z < 300) and (mouse_press[0] == True):
                    z = z + 10
                if (330 >= mouse[1] >= 295) and (310 >= mouse[0] >= 90) and (mouse_press[0] == True):
                    z = mouse[0] - 10
                pygame.mixer.music.set_volume((z - 80) / 220)
                z2 = z

                ###pfs###
                if fifteen_flag:
                    FPS = 15
                    fifteen_flag = False
                    continue
                if thirty_flag:
                    FPS = 30
                    thirty_flag = False
                    continue
                if sixty_flag:
                    FPS = 60
                    sixty_flag = False
                    continue

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

            elif home_flag:
                window.blit(background3, (x, y))

                ####Create Button####
                Button.button("play", 150, 300, 100, 50, green, (0, 255, 0), action="play")
                Button.button("setting", 150, 400, 100, 50, yellow, (255, 255, 0), action="setting")
                Button.button("quit", 150, 500, 100, 50, red, (255, 0, 0), action="quit")
                window.blit(sound_off, (0, 0))
                window.blit(sound_on, (50, 0))
                pygame.draw.line(window, black, (46, 6), (46, 42), 2)

                ####Mute button####
                if (42 >= mouse[0] >= 0) and (18 <= mouse[1] <= 55) and (mouse_press[0] == True):
                    pygame.mixer.music.pause()
                    z = 80

                if (89 >= mouse[0] >= 46) and (18 <= mouse[1] <= 55) and (mouse_press[0] == True):
                    pygame.mixer.music.unpause()
                    z = z2

                ####coins_Display#####
                Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)  # creating font object
                textSurf, Score = text_objects("score: %d" % game_score, Score_text)  # Using the font object
                Score.center = (200, 140)  # location of font object
                window.blit(textSurf, Score)  # putting the font object in Window panel

                #####draw the mouse here so is on top of everything else#####
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
