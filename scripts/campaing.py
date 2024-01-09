import pygame, sys
import utils.language as lang
import utils.config as config

class Campaing:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def campaing(self):
        dict_lang = lang.Language.set_lang(self, config.language)
    
        # load background images
        menu_background = pygame.transform.scale(
            pygame.image.load('assets/background/Map1.jpg').convert(),
            self.resolution
        )

    while True:
        # set frames
        self.clock.tick(self.fps)
        
        Menu_mouse_position = pygame.mouse.get_pos()
        
        # draw background
        self.screen.blit(menu_background, (0, 0))

        # draw menu text
        # self.screen.blit(menu_text, menu_text_rect)

        # update
        pygame.display.flip()