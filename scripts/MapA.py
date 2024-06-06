import pygame, sys
from utils.FogButton import FogButton
from scripts.MainMenu import MainMenu
from utils.Button import Button
from scripts.TeamView import TeamView
from scripts.events.MapAEvents import MapAEvents
import utils.Language as lang
import utils.Config as config

class MapA:
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
        events = MapAEvents(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, self.equipment)

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/MapA/MapA(Cave Entrace).jpg').convert(),
            self.resolution
        )

        #zone button variables
        zone_buttons = self.createFogButtons()
        activity_zone_buttons = [0, 1, 2, 11]
        disable_zone_buttons = []

        #quit button variables
        team_button_font = pygame.font.Font("assets/fonts/alagard.ttf", 30)
        team_button_base_color = "#a9b0c7"
        team_button_hover_color = "#ffffff"
        team_button = Button(None, (900,560), "Team", team_button_font, team_button_base_color, team_button_hover_color)
        
        next_map = True

        while next_map == True :
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

                    if zone_buttons[0].checkForInput(mouse_position) and 0 not in disable_zone_buttons and 0 in activity_zone_buttons:
                        event_response = events.zone1()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[1].checkForInput(mouse_position) and 1 not in disable_zone_buttons and 1 in activity_zone_buttons:
                        event_response = events.zone2()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[2].checkForInput(mouse_position) and 2 not in disable_zone_buttons and 2 in activity_zone_buttons:
                        event_response = events.zone3()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[3].checkForInput(mouse_position) and 3 not in disable_zone_buttons and 3 in activity_zone_buttons:
                        event_response = events.zone4()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[4].checkForInput(mouse_position) and 4 not in disable_zone_buttons and 4 in activity_zone_buttons:
                        event_response = events.zone5()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[5].checkForInput(mouse_position) and 5 not in disable_zone_buttons and 5 in activity_zone_buttons:
                        event_response = events.zone6()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[6].checkForInput(mouse_position) and 6 not in disable_zone_buttons and 6 in activity_zone_buttons:
                        event_response = events.zone7()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[7].checkForInput(mouse_position) and 7 not in disable_zone_buttons and 7 in activity_zone_buttons:
                        event_response = events.zone8()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[8].checkForInput(mouse_position) and 8 not in disable_zone_buttons and 8 in activity_zone_buttons:
                        event_response = events.zone9()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)

                    if zone_buttons[9].checkForInput(mouse_position) and 9 not in disable_zone_buttons and 9 in activity_zone_buttons:
                        event_response = events.zone10()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)
                    
                    if zone_buttons[10].checkForInput(mouse_position) and 10 not in disable_zone_buttons and 10 in activity_zone_buttons:
                        event_response = events.zone11()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)
                    
                    if zone_buttons[11].checkForInput(mouse_position) and 11 not in disable_zone_buttons and 11 in activity_zone_buttons:
                        event_response = events.zone12()
                        activity_zone_buttons.extend(event_response.activity_zone_buttons)
                        disable_zone_buttons.extend(event_response.disable_zone_buttons)    
                        next_map = False


            # update
            pygame.display.flip()
                        
    def createFogButtons(self):
        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 9)
        text_color = "#ffffff"
        text_hover = "#ff0000"
        fogButton_image = pygame.image.load('assets/buttons/zone_buttons/Zone_Layout.png')
        fogButton_image_format = pygame.transform.scale(fogButton_image, (100,80))

        zone1 = FogButton(fogButton_image_format, (300,85), "Pedra Brilhante", font, text_color, text_hover, True)
        zone2 = FogButton(fogButton_image_format, (170,220), "Botes recentes", font, text_color, text_hover, True)
        zone3 = FogButton(fogButton_image_format, (360,225), "Corredor", font, text_color, text_hover, True)
        zone4 = FogButton(fogButton_image_format, (75,110), "Ruínas", font, text_color, text_hover, True)
        zone5 = FogButton(fogButton_image_format, (120,540), "Santuário", font, text_color, text_hover, True)
        zone6 = FogButton(fogButton_image_format, (260,600), "Entulhos", font, text_color, text_hover, True)
        zone7 = FogButton(fogButton_image_format, (490,420), "Escavação", font, text_color, text_hover, True)
        zone8 = FogButton(fogButton_image_format, (650,565), "Acampamento", font, text_color, text_hover, True)
        zone9 = FogButton(fogButton_image_format, (800,555), "?", font, text_color,text_hover, True)
        zone10 = FogButton(fogButton_image_format, (325,310), "Presença na água", font, text_color, text_hover, True)
        zone11 = FogButton(fogButton_image_format, (695,125), "Ponte perigosa", font, text_color, text_hover, True)
        zone12 = FogButton(fogButton_image_format, (925,185), "Escadas", font, text_color, text_hover, True)

        return [zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9,
                zone10, zone11, zone12 ]
