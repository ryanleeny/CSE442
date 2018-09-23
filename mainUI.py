import pygame
import tkinter.messagebox
import bg


class button():
    def button(text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:

                if action == "15":
                    global fifteen_flag
                    fifteen_flag = True

                if action == "30":
                    global thirty_flag
                    thirty_flag = True

                if action == "60":
                    global sixty_flag
                    sixty_flag = True

                if action == "home":
                    global home_flag
                    home_flag = True

                if action == "setting":
                    #print("Setting Button Clicked")
                    global setting_flag
                    setting_flag = True

                if action == "play":
                    #print("Play Button Click, go to gameLoop")
                    global gaming_flag
                    gaming_flag = True

                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))
        button.text_to_button(text, black, x, y, width, height)

    def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
        textSurf, textRect = button.text_objects(msg, color, size)
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


class game():
    def gameflow(self):
        gameExit = False
        gameOver = False
        # while not gameExit:
        print("Game Playing")


class setting():
    def option(self):
        pygame.draw.line(window, white, (80, 300), (320, 300), 3)  # Draw a line
        window.blit(voice_col, (z, 289))
        window.blit(voice_low, (40, 277))
        window.blit(voice_high, (320, 277))
        window.blit(fps, (55, 380))
        button.button("15", 190, 380, 100, 50, gold, (255, 255, 255), action="15")
        button.button("30", 190, 450, 100, 50, gold, (255, 255, 255), action="30")
        button.button("60", 190, 520, 100, 50, gold, (255, 255, 255), action="60")
        button.button("", 336, 638, 50, 50, white, (255, 255, 255), action="home")
        window.blit(home, (350, 652))


class main(object):
    ####global functions here#####
    global text_objects, galaxy_background
    global window

    #####global varaible declaration here#####
    global black, white, green, red, gold, blue, yellow, game_score, home, background, background2, fps, voice_col,\
        voice_low, voice_high, sound_off, width, height, x, y, cursor1, home_flag, gaming_flag, setting_flag
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (34, 177, 76)
    yellow = (200, 200, 0)
    red = (200, 0, 0)
    gold = (227, 207, 87)
    blue = (23, 44, 225)
    width = 401  # Window width
    height = 700  # Window height
    game_score = 0  # score to display in the screen
    background = pygame.image.load('background.jpeg')
    background2 = pygame.image.load('bg2.jpeg')
    cursor1 = pygame.image.load('ship.png')  # very basic design on the cursor/ship, but can work on it later
    voice_low = pygame.image.load('vl.png')
    voice_high = pygame.image.load('vh.png')
    voice_col = pygame.image.load('vc.png')
    sound_off = pygame.image.load('so.png')
    home = pygame.image.load('home.png')
    fps = pygame.image.load('fps.png')
    gaming_flag = False
    setting_flag = False
    home_flag = False

    ####Unuse Declaration#####
    x = width * 1  # x and y is the position of background img
    y = height * 1

    #####The font of button object#####
    def text_objects(text, font):
        textSurface = font.render(text, True, gold)
        return textSurface, textSurface.get_rect()

    def __create_sprites(self):
        self.__create_background()

    def __create_background(self):
        bg1 = bg.Background()
        bg2 = bg.Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(window)

    ####Below initialize the GUI (Before LOOP)#####
    def __init__(self):
        global z,f
        z = 180
        f = 60
        self.__create_sprites()

        ####main loop of the GUI#####
        gameLoop = True  # ;This the the loop of the main game, FALSE to exit the loop
        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #####add backcground moving alone with mouse#####
            mouse = pygame.mouse.get_pos()
            global x, y, fifteen_flag, thirty_flag, sixty_flag
            x = mouse[0] * -0.05
            y = mouse[1] * -0.05
            #window.blit(background, (x, y))
            fifteen_flag = False #fps#
            thirty_flag = False
            sixty_flag = False

            #####mouse######
            mx = mouse[0] - cursor1.get_width() / 2
            my = mouse[1] - cursor1.get_height() / 2
            pygame.mouse.set_visible(False)

            #####Making button change color by matching the button location#####
            mouse = pygame.mouse.get_pos()

            #####Add Mouse press detection######
            mousepress = pygame.mouse.get_pressed()

            if gaming_flag:
                # function for creat enmies
                # fuction for check colid
                # function for update screen
                self.__update_sprites()

            elif setting_flag:
                window.blit(background2, (x, y)) #set up the background
                setting.option(self)  #branch to function named option() from class setting

                ###---voice control---###
                if (mouse[0] >= 48) and (mouse[0] <= 77) and (mouse[1] <= 328) and (mouse[1] >= 300) and (z > 80) and (mousepress[0] == True):
                    z = z - 10
                if (mouse[0] >= 320) and (mouse[0] <= 360) and (mouse[1] <= 330) and (mouse[1] >= 296) and (z < 300) and (mousepress[0] == True):
                    z = z + 10

                ###pfs###
                if fifteen_flag:
                    f = 15
                    continue
                if thirty_flag:
                    f = 30
                    continue
                if sixty_flag:
                    f = 60
                    continue

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

                ###back to main menu###
                if home_flag:
                    #main.__init__(self)
                    #setting_flag = False
                    #continue
                    break

            else:
                window.blit(background2, (x, y))
                ####Create Button####
                button.button("play", 150, 350, 100, 50, green, (0, 255, 0), action="play")
                button.button("setting", 150, 450, 100, 50, yellow, (255, 255, 0), action="setting")
                button.button("quit", 150, 550, 100, 50, red, (255, 0, 0), action="quit")
                window.blit(sound_off, (350,0))

                ####coins_Display#####
                Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)  # creating font object
                textSurf, Score = text_objects("score: %d" % game_score, Score_text)  # Using the font object
                Score.center = (200, 240)  # location of font object
                window.blit(textSurf, Score)  # putting the font object in Window panel

                #####draw the mouse here so is on top of everything else#####
                window.blit(cursor1, (mx, my))

            #####refresh everything#####
            clock.tick(f)
            pygame.display.update()

pygame.quit()

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    game = main()
