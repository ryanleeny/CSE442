import pygame


class main(object):
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Window")
        black = (0,0,0)
        gameLoop=True

        while gameLoop:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    gameLoop=False
            window.fill(black)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    game = main()