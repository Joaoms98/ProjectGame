import pygame, sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button

class MainMenu:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def run(self):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        
        # music
        theme_music_sfx = pygame.mixer.Sound('assets/music/MainMenuMusic.mp3')
        theme_music_sfx_volume = config.volume / 100
        theme_music_sfx.set_volume(theme_music_sfx_volume)

        theme_music_sfx.play()

        #load background
        main_menu_background = pygame.transform.scale(
            pygame.image.load('assets/background/background_main_menu1.jpg').convert(),
            self.resolution
        )
        play_screen_background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            (500,400)
        )
        options_screen_background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            (500,400)
        )
        how_to_play_screen_background = pygame.transform.scale(
            pygame.image.load('assets/background/how_to_play_image.jpg').convert(),
            (500,400)
        )
        
        #load buttons
        main_menu_buttons = self.createMainMenuButtons(dict_lang)
        play_screen_buttons = self.createPlayScreenButtons(dict_lang)
        options_screen_buttons = self.createOptionsScreenButtons(dict_lang)
        how_to_play_screen_buttons = self.createHowToPlayScreenButtons(dict_lang)

        #apply config
        apply_changes_config = False

        #validators for screens
        play_screen = False 
        options_screen = False
        how_to_play_screen = False
        how_to_play_screen_next_tips = 0
        volumeAppearance= self.buttonsAppearance()
        volume = volumeAppearance[1].render(f'{config.volume}', True, volumeAppearance[2])
        
        while True:
            # set frames
            self.clock.tick(self.fps)
            
            mouse_position = pygame.mouse.get_pos()

            # Validator    
            if options_screen == False and play_screen == False and how_to_play_screen == False:
                self.screen.blit(main_menu_background, (0, 0))

            #### DRAW BUTTONS ####            
           #### PLAY SCREEN BUTTONS ####
            if play_screen == True:
                self.screen.blit(play_screen_background, (350, 100))
                for button in play_screen_buttons:
                    button.changeColor(mouse_position)
                    button.update(self.screen)
            #### OPTIONS SCREEN BUTTONS ####
            if options_screen == True:
                self.screen.blit(options_screen_background, (350, 100))
                self.screen.blit(volume, (590,200))

                for button in options_screen_buttons:
                    button.changeColor(mouse_position)
                    button.update(self.screen)

            #### HOW TO PLAY SCREEN ####
            if how_to_play_screen == True and how_to_play_screen_next_tips == 0:
                self.screen.blit(how_to_play_screen_background, (350, 100))
                for button in how_to_play_screen_buttons:
                    button.changeColor(mouse_position)
                    button.update(self.screen)
            
            #### MAIN MENU BUTTONS ####
            for button in main_menu_buttons:
                button.changeColor(mouse_position)
                button.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #### MAIN MENU #### 
                    if main_menu_buttons[0].checkForInput(mouse_position):
                        if play_screen == True:
                            play_screen = False
                        else:
                            how_to_play_screen = False
                            options_screen = False
                            play_screen = True
                    if main_menu_buttons[1].checkForInput(mouse_position):
                        if options_screen == True:
                            options_screen = False
                        else:
                            play_screen = False 
                            how_to_play_screen = False
                            options_screen = True
                    if main_menu_buttons[2].checkForInput(mouse_position):
                        if how_to_play_screen == True:
                            how_to_play_screen = False
                            how_to_play_screen_next_tips = 0
                        else:
                            play_screen = False 
                            options_screen = False
                            how_to_play_screen = True
                    if main_menu_buttons[3].checkForInput(mouse_position):
                        pygame.quit()
                        sys.exit()

                    #### PLAY SCREEN ####
                    if play_screen == True:
                        if play_screen_buttons[0].checkForInput(mouse_position):
                            return

                    #### OPTIONS SCREEN ####
                    if options_screen == True:
                        if options_screen_buttons[0].checkForInput(mouse_position):
                            config.volume += 10
                            if config.volume > 100:
                                config.volume = 100
                        if options_screen_buttons[1].checkForInput(mouse_position):
                            config.volume -= 10
                            if config.volume < 1:
                                config.volume = 0
                        volume = volumeAppearance[1].render(f'{config.volume}', True, volumeAppearance[2])

                        if options_screen_buttons[2].checkForInput(mouse_position):
                            if config.language == 'English':
                                config.language = 'Português-Brasil'
                                buttonsAppearance = self.buttonsAppearance()
                                options_screen_buttons[2] = Button(buttonsAppearance[0], (590,300), f"{config.language}", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
                            elif config.language == 'Português-Brasil':
                                config.language = 'English'
                                buttonsAppearance = self.buttonsAppearance()
                                options_screen_buttons[2] = Button(buttonsAppearance[0], (590,300), f"{config.language}", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
                           
                        if options_screen_buttons[3].checkForInput(mouse_position):
                            dict_lang = lang.Language.set_lang(self, config.language)
                            theme_music_sfx_volume = config.volume/100
                            theme_music_sfx.set_volume(theme_music_sfx_volume)
                            main_menu_buttons = self.createMainMenuButtons(dict_lang)
                            play_screen_buttons = self.createPlayScreenButtons(dict_lang)
                            options_screen_buttons = self.createOptionsScreenButtons(dict_lang)
                            how_to_play_screen_buttons = self.createHowToPlayScreenButtons(dict_lang)
                            options_screen = False

                    #### HOW TO PLAY SCREEN ####
                    if how_to_play_screen == True:
                        if how_to_play_screen_buttons[0].checkForInput(mouse_position):
                            how_to_play_screen_next_tips = how_to_play_screen_next_tips + 1
                            if how_to_play_screen_next_tips >= 3 :
                                how_to_play_screen_next_tips = 0
                        if how_to_play_screen_buttons[1].checkForInput(mouse_position):
                            how_to_play_screen_next_tips = how_to_play_screen_next_tips - 1
                            if how_to_play_screen_next_tips <= -1:
                                how_to_play_screen_next_tips = 2

            # update
            pygame.display.flip()
    
    def createMainMenuButtons(self, lang):
        
        buttonsAppearance = self.buttonsAppearance()

        play_button = Button(buttonsAppearance[0], (140,150), lang['play'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        options_button = Button(buttonsAppearance[0], (140,250), lang['options'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        how_to_play_button = Button(buttonsAppearance[0], (140,350), lang['how_to_play'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        quit_button = Button(buttonsAppearance[0], (140,450), lang['exit'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])

        return [play_button, options_button, how_to_play_button, quit_button]

    def createPlayScreenButtons(self, lang):

        buttonsAppearance = self.buttonsAppearance()
        new_game_button = Button(buttonsAppearance[0], (600,250), lang['new_game'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        
        return [new_game_button]

    def createOptionsScreenButtons(self, lang):
        buttonsAppearance = self.buttonsAppearance()

        raise_volume_button = Button(buttonsAppearance[0], (750,200), f">", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        lower_volume_button = Button(buttonsAppearance[0], (450,200), f"<", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        language_button = Button(buttonsAppearance[0], (590,300), f"{config.language}", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        apply_button = Button(buttonsAppearance[0], (590,400), lang['apply'], buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        
        return [raise_volume_button, lower_volume_button, language_button, apply_button]
    
    def createHowToPlayScreenButtons(self, lang):
        
        buttonsAppearance = self.buttonsAppearance()

        next_info_button =  Button(None, (0,0), "", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])
        previous_info_button = Button(None, (0,0), "", buttonsAppearance[1], buttonsAppearance[2], buttonsAppearance[3])

        return [next_info_button, previous_info_button]
    
    def buttonsAppearance(self):
        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 15)
        text_color = "#ffffff"
        text_hover = "#ff0000"
        #button image
        button_image = pygame.image.load("assets/buttons/decision_button.png")
        button_image_format = pygame.transform.scale(button_image,(150,50))

        return [button_image_format, font, text_color, text_hover]


        

            