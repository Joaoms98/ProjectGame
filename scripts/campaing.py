import pygame, sys
from scripts.events import Events
from utils.fogbutton import FogButton
import utils.language as lang
import utils.config as config

class Campaing:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def run(self):
        # Objects instances
        dict_lang = lang.Language.set_lang(self, config.language)
        events = Events(self.screen, self.screen_rect, self.fps, self.resolution)


        # load background images
        campaing_background = pygame.transform.scale(
            pygame.image.load('assets/background/Map1.jpg').convert(),
            self.resolution
        )        

        # menu text variables
        font_level = pygame.font.Font("assets/fonts/alagard.ttf", 20)        
        campaing_text = font_level.render(dict_lang["campaing_text_level"], True, "#ff0000")
        campaing_text_rect = campaing_text.get_rect(center=(self.screen_rect.centerx, 350))

        # menu text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30)        

        # menu FogButton text variables
        campaing_text_color = "#ff0000"
        hover_text_color = "White"
        fogbutton_image = pygame.image.load('assets/buttons/zone_buttons/Zone_Layout.png')

        #Zones FogButton
        zone1_FogButton = FogButton(fogbutton_image, (150, 100), "Explorar", font, campaing_text_color, hover_text_color)
        zone2_FogButton = FogButton(fogbutton_image, (500, 100), "Explorar", font, campaing_text_color, hover_text_color)
        zone3_FogButton = FogButton(fogbutton_image, (850, 100), "Explorar", font, campaing_text_color, hover_text_color)
        zone4_FogButton = FogButton(fogbutton_image, (150, 350), "Explorar", font, campaing_text_color, hover_text_color)
        zone6_FogButton = FogButton(fogbutton_image, (850, 350), "Explorar", font, campaing_text_color, hover_text_color)
        zone7_FogButton = FogButton(fogbutton_image, (150, 600), "Explorar", font, campaing_text_color, hover_text_color)
        zone8_FogButton = FogButton(fogbutton_image, (500, 600), "Explorar", font, campaing_text_color, hover_text_color)
        zone9_FogButton = FogButton(fogbutton_image, (850, 600), "Explorar", font, campaing_text_color, hover_text_color)
        
        # load PopUp
        show_popup = pygame.transform.scale(
            pygame.image.load('assets/popups/fogbuttonpopup.png').convert(),
            (1000,700)
        )
        
        popup_validator = False

        while True:
            # set frames
            self.clock.tick(self.fps)
            
            campaing_mouse_position = pygame.mouse.get_pos()
            
            if popup_validator == False:
                # draw background
                self.screen.blit(campaing_background, (0, 0))
                # draw menu text
                self.screen.blit(campaing_text, campaing_text_rect)    
                # draw FogButton
                for Fogbutton in [
                    zone1_FogButton,
                    zone2_FogButton,
                    zone3_FogButton,
                    zone4_FogButton,
                    zone6_FogButton,
                    zone7_FogButton,
                    zone8_FogButton,
                    zone9_FogButton]:
                    Fogbutton.changeColor(campaing_mouse_position)
                    if Fogbutton.disable_button == False:
                        Fogbutton.update(self.screen)
            else:
                self.screen.blit(show_popup, (0,0))
                
             # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if zone1_FogButton.checkForInput(campaing_mouse_position):
                        popup_validator = True
                        events.run()
                    # if zone2_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone3_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone4_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone6_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone7_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone8_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')
                    # if zone9_FogButton.checkForInput(campaing_mouse_position):
                    #     print('play')


            # update
            pygame.display.flip()

    #def decisionButton(self):
