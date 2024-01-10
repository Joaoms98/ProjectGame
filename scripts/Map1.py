import pygame, sys
from scripts.PopUpEvent import PopUpEvent
from services.EventService import EventService
from utils.fogbutton import FogButton
import utils.language as lang
import utils.config as config

class Map1:
    def __init__(self, screen, screen_rect, fps, resolution, allies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.clock = pygame.time.Clock()

    def run(self):
        # Objects instances
        dict_lang = lang.Language.set_lang(self, config.language)
        pop_up_event = PopUpEvent(self.screen, self.screen_rect, self.fps, self.resolution, self.allies)

        # load background images
        campaing_background = pygame.transform.scale(
            pygame.image.load('assets/background/Map1.jpg').convert(),
            self.resolution
        )

        # FogButton text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30) 
        fogbutton_image = pygame.transform.scale(
            pygame.image.load('assets/buttons/zone_buttons/Zone_Layout.png').convert(),
            (100, 100)
        )

        zone1_FogButton = FogButton(fogbutton_image, (300, 500), "Explorar", font, (0,255,0), (255,0,0))

        while True:
            # set frames
            self.clock.tick(self.fps)
            
            campaing_mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(campaing_background, (0, 0))

            # draw FogButton
            for Fogbutton in [zone1_FogButton]:
                Fogbutton.changeColor(campaing_mouse_position)
                Fogbutton.update(self.screen)

             # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if zone1_FogButton.checkForInput(campaing_mouse_position):
                        pop_up_event.run("A1_1")

            # update
            pygame.display.flip()
