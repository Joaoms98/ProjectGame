import pygame, sys
from scripts.EventHandler import EventHandler
from utils.FogButton import FogButton
from scripts.MainMenu import Menu
from utils.Button import Button
from scripts.TeamView import TeamView
import utils.Language as lang
import utils.Config as config

class MapB:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.clock = pygame.time.Clock()

    def run(self):
        # Objects instances
        dict_lang = lang.Language.set_lang(self, config.language)
        event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, self.equipment)
        #menu = Menu(self.screen, self.screen_rect, config.fps, config.resolution)
        team_view = TeamView(self.screen, self.screen_rect, self.fps, self.resolution, self.allies)

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/MapB/MapB(The Cristal Cave).jpg').convert(),
            self.resolution
        )

        # FogButton text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30) 
        fogButton_image = 'assets/buttons/zone_buttons/Zone_Layout.png' 
        zone1_image = pygame.transform.scale(
            pygame.image.load(fogButton_image),(82, 70))
        zone2_image = pygame.transform.scale(
            pygame.image.load(fogButton_image),(120, 70))
        zone3_image = pygame.transform.scale(
            pygame.image.load(fogButton_image).convert(),(120, 139))

        zone1_FogButton = FogButton(zone1_image, (360, 450), "Evento 1", font, (0,255,0), (255,0,0))
        zone1_completed = False
        zone1_FogButton.zone_activy = True
        zone2_FogButton = FogButton(zone2_image, (380, 350), "?", font, (0,255,0), (255,0,0))
        zone2_completed = False
        zone3_FogButton = FogButton(zone3_image, (380, 150), "?", font, (0,255,0), (255,0,0))
        zone3_completed = False

        #quit button variables
        team_button_font = pygame.font.Font("assets/fonts/alagard.ttf", 30)
        team_button_base_color = "#a9b0c7"
        team_button_hover_color = "#ffffff"
        team_button = Button(None, (900,560), "Team", team_button_font, team_button_base_color, team_button_hover_color)

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

            self.unlockEvent(zone2_FogButton,zone2_completed,mouse_position)

            # draw Team button
            team_button.changeColor(mouse_position)
            team_button.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if team_button.checkForInput(mouse_position):
                        team_view.run()
                    if zone1_completed == False:
                        if zone1_FogButton.checkForInput(mouse_position):
                            event_response = event_handler.run("A1_1")
                            zone1_completed = event_response.completed
                            self.allies = event_response.allies
                            if zone1_completed == True:
                                zone2_FogButton.zone_activy = True
                    if zone2_completed == False:
                        if zone2_FogButton.checkForInput(mouse_position):
                            event_response = event_handler.run("A2_1")
                            zone2_completed = event_response.completed
                            self.allies = event_response.allies

            # update
            pygame.display.flip()
    def unlockEvent(self, zone, zone_completed, mouse_position):       
            if zone.zone_activy == False:
                zone.update(self.screen)
            elif zone_completed == False:
                    zone.changeColor(mouse_position)
                    zone.update(self.screen)

    def fogButtonsAppearance(self):
        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 15)
        text_color = "#ffffff"
        text_hover = "#ff0000"
        fogButton_image = 'assets/buttons/zone_buttons/Zone_Layout.png' 
        fogButton_image_format = pygame.transform.scale(fogButton_image,(150,50))

        return [fogButton_image_format,font, text_color, text_hover]
    
    
    def createFogButtons(self,lang):

        appearance = self.fogButtonsAppearance()

        zone1 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone2 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone3 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone4 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone5 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone6 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone7 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone8 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone9 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone10 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone11 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])
        zone12 = FogButton(appearance[0], (140,150), "?", appearance[1], appearance[2], appearance[3])


    
