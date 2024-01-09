import pygame, sys
from utils.campaingbutton import CampaingButton
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

        # menu text variables
        font_level = pygame.font.Font("assets/fonts/alagard.ttf", 20)        
        menu_text = font_level.render(dict_lang["campaing_text_level"], True, "#11ebeb")
        menu_text_rect = menu_text.get_rect(center=(self.screen_rect.centerx, 50))

        # menu text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30)        

        # menu CampaingButton text variables
        menu_text_color = "#ff0000"
        hover_text_color = "White"
        image = pygame.image.load("assets/buttons/zone_buttons/Zone_Layout.png")

        #Zones CampaingButton
        zone1_CampaingButton = CampaingButton(image, (150, 100), "Explorar", font, menu_text_color, hover_text_color)
        zone2_CampaingButton = CampaingButton(image, (500, 100), "Explorar", font, menu_text_color, hover_text_color)
        zone3_CampaingButton = CampaingButton(image, (850, 100), "Explorar", font, menu_text_color, hover_text_color)
        zone4_CampaingButton = CampaingButton(image, (150, 350), "Explorar", font, menu_text_color, hover_text_color)
        zone6_CampaingButton = CampaingButton(image, (850, 350), "Explorar", font, menu_text_color, hover_text_color)
        zone7_CampaingButton = CampaingButton(image, (150, 600), "Explorar", font, menu_text_color, hover_text_color)
        zone8_CampaingButton = CampaingButton(image, (500, 600), "Explorar", font, menu_text_color, hover_text_color)
        zone9_CampaingButton = CampaingButton(image, (850, 600), "Explorar", font, menu_text_color, hover_text_color)
        
        while True:
            # set frames
            self.clock.tick(self.fps)
            
            Menu_mouse_position = pygame.mouse.get_pos()
            
            # draw background
            self.screen.blit(menu_background, (0, 0))

            # draw menu text
            self.screen.blit(menu_text, menu_text_rect)

             # draw CampaingButton
            for CampaingButton in [zone1_CampaingButton, zone2_CampaingButton, zone3_CampaingButton,
             zone4_CampaingButton,zone6_CampaingButton,zone7_CampaingButton,
             zone8_CampaingButton,zone9_CampaingButton]:
                CampaingButton.changeColor(Menu_mouse_position)
                if CampaingButton.disable_button == False:
                    CampaingButton.update(self.screen)
             
             # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if zone1_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone2_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone3_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone4_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone6_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone7_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone8_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')
                    if zone9_CampaingButton.checkForInput(Menu_mouse_position):
                        print('play')


            # update
            pygame.display.flip()