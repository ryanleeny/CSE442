import pygame
import tkinter.messagebox


class button():
    def button(text, x, y, width, height, inactive_color, active_color, action = None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(window, active_color, (x,y,width,height))
            if click[0] == 1 and action != None:
                if action == "setting":
                    print("Setting Button Clicked")

                if action == "play":
                    print("Play Button Click, go to gameLoop")
                    global gaming_flag
                    gaming_flag = True

                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(window, inactive_color, (x,y,width,height))
        button.text_to_button(text,black,x,y,width,height)

    def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
        textSurf, textRect = button.text_objects(msg,color,size)
        textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
        window.blit(textSurf, textRect)

    def text_objects(text, color,size = "small"):
        smallfont = pygame.font.SysFont("comicsansms", 25)
        medfont = pygame.font.SysFont("comicsansms", 50)
        argefont = pygame.font.SysFont("comicsansms", 85)
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        if size == "medium":
            textSurface = medfont.render(text, True, color)
        if size == "large":
            textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

class game():
    def gameLoop():
        gameExit = False
        gameOver = False
        print ("Game Playing")

class main(object):
    ####global functions here#####
    global text_objects, galaxy_background
    global window

    #####global varaible declaration here#####
    global black,white,green,red,gold,blue,game_score,background,width,height,x,y,cursor1,Fire_In_The_Hole,gaming_flag
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    gold =(227,207,87)
    blue =(23,44,225)
    width = 401#Window width
    height = 700#Window height
    game_score = 0#score to display in the screen
    background = pygame.image.load('background.jpeg')
    cursor1 =pygame.image.load('ship.png') #very basic design on the cursor/ship, but can work on it later
    gaming_flag = False

    ####True mean the button is being pressed####
    Fire_In_The_Hole = False
    Score_Button = False
    Setting_Button = False

    ####Unuse Declaration#####
    x=width*1 #x and y is the position of background img
    y=height*1

    #####The font of button object#####
    def text_objects(text, font):
        textSurface = font.render(text, True, gold)
        return textSurface, textSurface.get_rect()

    ####Below initialize the GUI (Before LOOP)#####
    def __init__(self):
        red = (200,0,0)
        light_red = (255,0,0)
        yellow = (200,200,0)
        light_yellow = (255,255,0)
        green = (34,177,76)
        light_green = (0,255,0)

        ####main loop of the GUI#####
        gameLoop = True  # ;This the the loop of the main game, FALSE to exit the loop
        while gameLoop:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                        gameLoop=False

            #####add backcground moving alone with mouse#####
            mouse = pygame.mouse.get_pos()
            global x,y
            x=mouse[0]*-0.05
            y=mouse[1]*-0.05
            window.blit(background, (x, y))

            #####mouse######
            mx=mouse[0]-cursor1.get_width()/2
            my=mouse[1]-cursor1.get_height()/2
            pygame.mouse.set_visible(False)

            #####Making button change color by matching the button location#####
            mouse = pygame.mouse.get_pos()
       
            #####Add Mouse press detection######
            mousepress =pygame.mouse.get_pressed()

            global Fire_In_The_Hole, Score_Button,Setting_Button
            Fire_In_The_Hole = False## Button press reset##

            ####Create Button####
            if gaming_flag:
                pass
            else:
                button.button("play", 150, 350, 100, 50, green, (0,255,0), action="play")
                button.button("setting", 150, 450, 100, 50, yellow, (255,255,0), action="setting")
                button.button("quit", 150, 550, 100, 50, red, (255,0,0), action ="quit")

            ####coins_Display#####
            Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)#creating font object
            textSurf, Score = text_objects("score: %d" %game_score, Score_text)# Using the font object
            Score.center = (200, 100)# location of font object
            window.blit(textSurf, Score)# putting the font object in Window panel

            #####draw the mouse here so is on top of everything else#####
            window.blit(cursor1, (mx, my))
            #####refresh everything#####
            clock.tick(60)
            # print(Fire_In_The_Hole)
            pygame.display.update()
pygame.quit()

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Galaga")
    clock =pygame.time.Clock()
    game = main()