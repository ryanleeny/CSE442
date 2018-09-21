import pygame
import tkinter.messagebox


class main(object):
    ####global functions here#####
    global text_objects, galaxy_background

    #####global varaible declaration here#####
    global black,white,green,red,gold,blue,game_score,background,width,height,x,y,cursor1,Fire_In_The_Hole
    global Score_Button,Setting_Button

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

##################True mean the button is being pressed##############
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
        pygame.init()
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Galaga")
        clock =pygame.time.Clock()



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
            pygame.draw.rect(window, white, (150, 350, 100, 50))#;;;;Draw rec Left Button
            pygame.draw.rect(window, white, (150, 550, 100, 50))#;;;;Draw rec Right Button
            pygame.draw.rect(window, white, (150, 450, 100, 50))# ;;;;Draw rec last Button
            ###################mouse##############
            mx=mouse[0]-cursor1.get_width()/2
            my=mouse[1]-cursor1.get_height()/2
            pygame.mouse.set_visible(False)
            #####Making button change color by matching the button location#####
            mouse = pygame.mouse.get_pos()
            #print(mouse)#;printing the mouse position
            #######Add Mouse press detection########
            mousepress =pygame.mouse.get_pressed()

            global Fire_In_The_Hole, Score_Button,Setting_Button
            Fire_In_The_Hole = False## Button press reset##
            pygame.draw.rect(window, red, (150, 350, 100, 50))  # ;Default color of left button
            if 150 + 100 > mouse[0] > 150 and 350 + 50 > mouse[1] > 350:
                if mousepress[0]==True:
                    Fire_In_The_Hole =True
                    print (Fire_In_The_Hole)
                    pygame.draw.rect(window, white, (150, 350, 100, 50))###color when mouse is inside left button

            Setting_Button = False
            pygame.draw.rect(window, blue, (150, 550, 100, 50))  ###Default color of right button
            if 150 + 100 > mouse[0] > 150 and 550 + 50 > mouse[1] > 550:
                if mousepress[0] == True:
                    Setting_Button = True
                    pygame.draw.rect(window, white, (150, 550, 100, 50))###color when mosue is inside right button

            Score_Button = False
            pygame.draw.rect(window, green, (150, 450, 100, 50))
            if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
                if mousepress[0]==True:
                    Score_Button = True
                    pygame.draw.rect(window, white, (150, 450, 100, 50))###color when mouse is inside left button



            ####WRITE TO THE BUTTONS#####
            buttontext=pygame.font.Font("chela-one/ChelaOne-Regular.ttf",13)
            textSurf, Leftbutton = text_objects("Fire In The Hole", buttontext)
            Leftbutton.center = ((150 + (100 / 2)), (350 + (50 / 2)))
            window.blit(textSurf, Leftbutton)
            textSurf, Rightbutton = text_objects("Setting", buttontext)
            Rightbutton.center = ((150 + (100 / 2)), (550 + (50 / 2)))
            window.blit(textSurf, Rightbutton)
            textSurf, lastbutton = text_objects("Score", buttontext)
            lastbutton.center = ((150 + (100 / 2)), (450 + (50 / 2)))
            window.blit(textSurf, lastbutton)

            ####coins_Display#####
            Score_text = pygame.font.Font("chela-one/ChelaOne-Regular.ttf", 40)#creating font object
            textSurf, Score = text_objects("score: %d" %game_score, Score_text)# Using the font object
            Score.center = (200, 100)# location of font object
            window.blit(textSurf, Score)# putting the font object in Window panel

            #####draw the mouse here so is on top of everything else#####
            window.blit(cursor1, (mx, my))
            #####refresh everything#####
            clock.tick(60)
            print(Fire_In_The_Hole)
            pygame.display.update()

            ####Example how to use the mouse press Varaible#####
            if Fire_In_The_Hole==True:
                root=tkinter.Tk()
                root.withdraw()
                tkinter.messagebox.showwarning('Warning', 'warning you pressed an empty button',)

            if Score_Button == True:
                root = tkinter.Tk()
                root.withdraw()
                tkinter.messagebox.showwarning('Error', 'developer is too broke to implement this function', )

            if Setting_Button == True:
                root = tkinter.Tk()
                root.withdraw()
                tkinter.messagebox.showinfo('info', 'Change your setting in your own devices', )



pygame.quit()



if __name__ == '__main__':
    game = main()

