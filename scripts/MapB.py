import pygame, sys
from utils.FogButton import FogButton
from scripts.MainMenu import Menu
from utils.Button import Button
from scripts.TeamView import TeamView
from scripts.events.MapBEvents import MapBEvents
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
        team_view = TeamView(self.screen, self.screen_rect, self.fps, self.resolution, self.allies)
        events = MapBEvents(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, self.equipment)

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/MapB/MapB(The Cristal Cave).jpg').convert(),
            self.resolution
        )

        #zone button variables
        zone_buttons = self.createFogButtons()
        activity_zone_buttons = [0]
        disable_zone_buttons = []

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
            for i, button in enumerate(zone_buttons):
                if i in activity_zone_buttons:
                    button.changeColor(mouse_position)

                if i not in disable_zone_buttons:
                    button.update(self.screen)

            # draw Team button
            team_button.update(self.screen)
            team_button.changeColor(mouse_position)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if team_button.checkForInput(mouse_position):
                        team_view.run()
                    
                    if zone_buttons[0].checkForInput(mouse_position) and 0 not in disable_zone_buttons and 0 in activity_zone_buttons:
                        event_response = events.zone1()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

            # update
            pygame.display.flip()

    def createFogButtons(self):
        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 15)
        text_color = "#ffffff"
        text_hover = "#ff0000"
        fogButton_image = pygame.image.load('assets/buttons/zone_buttons/Zone_Layout.png')
        fogButton_image_format = pygame.transform.scale(fogButton_image, (100,80))

        zone1 = FogButton(fogButton_image_format, (900,310), "1", font, text_color, text_hover, True)
        zone2 = FogButton(fogButton_image_format, (800,150), "2", font, text_color, text_hover, True)
        zone3 = FogButton(fogButton_image_format, (680,280), "3", font, text_color, text_hover, True)
        zone4 = FogButton(fogButton_image_format, (800,400), "4", font, text_color, text_hover)
        zone5 = FogButton(fogButton_image_format, (600,400), "5", font, text_color, text_hover)
        zone6 = FogButton(fogButton_image_format, (600,150), "6", font, text_color, text_hover)
        zone7 = FogButton(fogButton_image_format, (400,400), "7", font, text_color, text_hover)
        zone8 = FogButton(fogButton_image_format, (140,150), "8", font, text_color, text_hover)
        zone9 = FogButton(fogButton_image_format, (140,150), "9", font, text_color,text_hover)
        zone10 = FogButton(fogButton_image_format, (140,150), "10", font, text_color, text_hover)
        zone11 = FogButton(fogButton_image_format, (140,150), "11", font, text_color, text_hover)
        zone12 = FogButton(fogButton_image_format, (140,150), "12", font, text_color, text_hover)
        zone13 = FogButton(fogButton_image_format, (140,150), "13", font, text_color, text_hover)
        zone14 = FogButton(fogButton_image_format, (140,150), "14", font, text_color, text_hover)
        zone15 = FogButton(fogButton_image_format, (140,150), "15", font, text_color, text_hover)
        zone16 = FogButton(fogButton_image_format, (140,150), "16", font, text_color, text_hover)

        return [zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9,
                zone10, zone11, zone12, zone13, zone14, zone15,zone16 ]

    
