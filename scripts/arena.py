import pygame, sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from scripts.options import Options

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

        # load background images
        menu_background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

    while True:
        # set frames
        self.clock.tick(self.fps)
    
        # draw background
        self.screen.blit(menu_background, (0, 0))