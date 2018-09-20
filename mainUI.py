import pygame


class main(object):
    ####global functions here#####
    global text_objects, galaxy_background

    #####global varaible declaration here#####
    global black,white,green,red,gold,blue,game_score,background,width,height,x,y
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

            #####Making button change color by matching the button location#####
            mouse = pygame.mouse.get_pos()
            print(mouse)#;printing the mouse position

            if 150 + 100 > mouse[0] > 150 and 350 + 50 > mouse[1] > 350:
                pygame.draw.rect(window, white, (150, 350, 100, 50))###color when mouse is inside left button
            else:
                pygame.draw.rect(window, red, (150, 350, 100, 50))#;Default color of left button
            if 150 + 100 > mouse[0] > 150 and 550 + 50 > mouse[1] > 550:
                pygame.draw.rect(window, white, (150, 550, 100, 50))###color when mosue is inside right button
            else:
                pygame.draw.rect(window, blue, (150, 550, 100, 50))###Default color of right button
            if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(window, white, (150, 450, 100, 50))###color when mouse is inside left button
            else:
                pygame.draw.rect(window, green, (150, 450, 100, 50))

            ####WRITE TO THE BUTTONS#####
            buttontext=pygame.font.Font("freesansbold.ttf",13)
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
            Score_text = pygame.font.Font("freesansbold.ttf", 40)#creating font object
            textSurf, Score = text_objects("Money In My Bank: %d" %game_score, Score_text)# Using the font object
            Score.center = (200, 100)# location of font object
            window.blit(textSurf, Score)# putting the font object in Window panel


            #####refresh everything#####
            pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    game = main()

