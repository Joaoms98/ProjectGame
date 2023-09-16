import pygame, sys
from utils.button import Button
import utils.config as config

class Options:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def options(self):
        # load background images
        menu_background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 50) 

        # menu button text variables
        menu_text_color = "#1c90ad"
        hover_text_color = "White"
        button = pygame.Rect(100, 100, 50, 50)
        image = pygame.image.load("assets/Play Rect.png")

        resolution_button = Button(image, (self.screen_rect.centerx, self.screen_rect.top + 120), f"{config.resolution}", font, menu_text_color, hover_text_color)
        fps_button = Button(image, (self.screen_rect.centerx, self.screen_rect.top + 240), f"{config.fps}", font, menu_text_color, hover_text_color)
        apply_button = Button(image, (self.screen_rect.centerx, self.screen_rect.top + 460), "Aplicar", font, menu_text_color, hover_text_color)

        back_to_menu = False

        while True:
            # set frames
            self.clock.tick(self.fps)

            Menu_mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(menu_background, (0, 0))

            # draw button
            for button in [resolution_button, fps_button, apply_button]:
                button.changeColor(Menu_mouse_position)
                button.update(self.screen)
 
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Check which button was pressed and reset the values of global variables
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resolution_button.checkForInput(Menu_mouse_position):
                        if config.resolution == (800, 600):
                            config.resolution = (1360, 768)
                        else:
                            config.resolution = (800, 600)

                        resolution_button = Button(image, (self.screen_rect.centerx, self.screen_rect.top + 120), f"{config.resolution}", font, menu_text_color, hover_text_color)

                    if fps_button.checkForInput(Menu_mouse_position):
                        if config.fps == 30:
                            config.fps = 60
                        else:
                            config.fps = 30

                        fps_button = Button(image, (self.screen_rect.centerx, self.screen_rect.top + 240), f"{config.fps}", font, menu_text_color, hover_text_color)
                    
                    if apply_button.checkForInput(Menu_mouse_position):
                        back_to_menu = True

            if back_to_menu == True:
                break

            # update
            pygame.display.flip()