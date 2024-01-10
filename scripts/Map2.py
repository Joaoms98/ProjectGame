import pygame, sys
from scripts.EventHandler import EventHandler
from utils.fogbutton import FogButton
import utils.language as lang
import utils.config as config

class Map2:
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
        event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, self.allies)

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/Map2.png').convert(),
            self.resolution
        )

        # FogButton text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30) 
        fogButton_image = 'assets/buttons/zone_buttons/Zone_Layout.png' 
        zone1_image = pygame.transform.scale(
            pygame.image.load(fogButton_image).convert(),(82, 70))
        zone2_image = pygame.transform.scale(
            pygame.image.load(fogButton_image).convert(),(120, 70))
        zone3_image = pygame.transform.scale(
            pygame.image.load(fogButton_image).convert(),(120, 139))

        zone1_FogButton = FogButton(zone1_image, (360, 450), "?", font, (0,255,0), (255,0,0))
        zone1_completed = False
        zone2_FogButton = FogButton(zone2_image, (380, 350), "?", font, (0,255,0), (255,0,0))
        zone2_completed = False
        zone3_FogButton = FogButton(zone3_image, (380, 150), "?", font, (0,255,0), (255,0,0))
        zone3_completed = False


        while True:
            # set frames
            self.clock.tick(self.fps)
            
            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(background, (0, 0))

            # draw FogButton
            if zone1_completed == False:
                zone1_FogButton.changeColor(mouse_position)
                zone1_FogButton.update(self.screen)

            if zone2_completed == False:
                zone2_FogButton.changeColor(mouse_position)
                zone2_FogButton.update(self.screen)

             # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if zone1_completed == False:
                        if zone1_FogButton.checkForInput(mouse_position):
                            event_response = event_handler.run("A1_1")
                            zone1_completed = event_response.completed
                    if zone2_completed == False:
                        if zone2_FogButton.checkForInput(mouse_position):
                            event_response = event_handler.run("A2_1")
                            zone2_completed = event_response.completed


            # update
            pygame.display.flip()
