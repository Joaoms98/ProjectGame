import pygame, sys
from utils.FogButton import FogButton
from scripts.MainMenu import MainMenu
from utils.Button import Button
from scripts.TeamView import TeamView
from scripts.events.MapCEvents import MapCEvents
import utils.Language as lang
import utils.Config as config

class MapC:
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
        theme_music_sfx= pygame.mixer.Sound('assets/music/mapC_sound.mp3')
        theme_music_sfx_volume = (config.volume - 25) / 100
        theme_music_sfx.set_volume(theme_music_sfx_volume)
        theme_music_sfx.play(loops=10)

        dict_lang = lang.Language.set_lang(self, config.language)
        team_view = TeamView(self.screen, self.screen_rect, self.fps, self.resolution, self.allies)
        events = MapCEvents(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, self.equipment)

        # load background images
        background = pygame.transform.scale(
            pygame.image.load('assets/background/MapC/MapC(The City).jpg').convert(),
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
        team_button = Button(None, (900,50), "Equipe", team_button_font, team_button_base_color, team_button_hover_color)
        
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
                        pygame.quit()
                        sys.exit()


            # update
            pygame.display.flip()
                        
    def createFogButtons(self):
        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 9)
        text_color = "#ffffff"
        text_hover = "#ff0000"
        fogButton_image = pygame.image.load('assets/buttons/zone_buttons/Zone_Layout.png')
        fogButton_image_format = pygame.transform.scale(fogButton_image, (100,80))

        zone1 = FogButton(fogButton_image_format, (500,350), "Ao futuro", font, text_color, text_hover, True)


        return [zone1]
