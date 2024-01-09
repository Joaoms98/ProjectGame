import pygame, sys, textwrap
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox

class Arena:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def arena(self):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        text_box = TextBox(self.screen, 15, pygame.font.SysFont("arial", 15))

        player_picture = 'assets/portraits/portrait_test_1.jpeg'
        black_image = 'assets/background/black_image.jpg'

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

        #text
        text = "teste da caixa de mensagem, heloo testando e testando muito testado hihi"
        color = (255,0,0)

        portrait1 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )

        portrait2 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )

        portrait3 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )


        #enemie
        portrait4 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )

        portrait5 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )

        portrait6 = pygame.transform.scale(
            pygame.image.load(player_picture).convert(),
            (150, 150)
        )

        #prompt
        prompt = pygame.transform.scale(
            pygame.image.load(black_image).convert(),
            (650, 220)
        )

        while True:
            # set frames
            self.clock.tick(self.fps)

            # draw background
            self.screen.blit(background, (0, 0))

            # draw background
            self.screen.blit(portrait1, (15, 20))
            self.screen.blit(portrait2, (15, 171))
            self.screen.blit(portrait3, (15, 322))

            self.screen.blit(portrait4, (840, 20))
            self.screen.blit(portrait5, (840, 171))
            self.screen.blit(portrait6, (840, 322))

            self.screen.blit(prompt, (178, 470))

            # draw text_box
            text_box.draw(text, color)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # update
            pygame.display.flip()