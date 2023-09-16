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

        # setando as fontes
        font = pygame.font.Font("assets/fonts/font.ttf", 50) 

        # menu button text variables
        menu_text_color = "#1c90ad"
        hover_text_color = "White"
        button = pygame.Rect(100, 100, 50, 50)

        resolution_button = Button(None, (self.screen_rect.centerx, self.screen_rect.top + 200), f"{config.resolution}", font, menu_text_color, hover_text_color)
        raise_volume_button = Button(None, (self.screen_rect.centerx + 200, self.screen_rect.top + 470), f">", font, menu_text_color, hover_text_color)
        lowered_volume_button = Button(None, (self.screen_rect.centerx - 200, self.screen_rect.top + 470), f"<", font, menu_text_color, hover_text_color)
        apply_button = Button(None, (self.screen_rect.centerx, self.screen_rect.bottom - 100), "Aplicar", font, menu_text_color, hover_text_color)

        # -> menu text variables <- #

        # variáveis do texto 'resolução'
        menu_text_resolution = font.render("Resolução:", True, "#11ebeb")
        menu_text_resolution_rect = menu_text_resolution.get_rect(center=(self.screen_rect.centerx, self.screen_rect.top + 100))

        # variáveis do texto 'volume'
        menu_text_volume = font.render("Volume:", True, "#11ebeb")
        menu_text_volume_rect =  menu_text_volume.get_rect(center=(self.screen_rect.centerx, self.screen_rect.top + 400))

        # variáveis do 'volume' que é alterado a cada click
        volume = font.render(f'{config.volume}', True, "#1c90ad")
        volume_rect =  menu_text_volume.get_rect(center=(self.screen_rect.centerx + 130, self.screen_rect.top + 470))

        back_to_menu = False

        while True:
            # setando os frames
            self.clock.tick(self.fps)

            Menu_mouse_position = pygame.mouse.get_pos()

            # printar o brackground
            self.screen.blit(menu_background, (0, 0))

            # printar os botões
            for button in [resolution_button, raise_volume_button, lowered_volume_button, apply_button]:
                button.changeColor(Menu_mouse_position)
                button.update(self.screen)

            # printas os textos da tela
            self.screen.blit(menu_text_resolution, menu_text_resolution_rect)
            self.screen.blit(menu_text_volume, menu_text_volume_rect)
            self.screen.blit(volume, volume_rect)

            # verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Check which button was pressed and reset the values of global variables
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resolution_button.checkForInput(Menu_mouse_position):
                        if config.resolution == (800, 600):
                            config.resolution = (1024, 768)
                        elif config.resolution == (1024, 768):
                            config.resolution = (1280, 760)
                        elif config.resolution == (1280, 760):
                            config.resolution = (1360, 768)
                        elif config.resolution == (1360, 768):
                            config.resolution = (1600, 900)
                        elif config.resolution == (1600, 900):
                            config.resolution = (1920, 1080)
                        elif config.resolution == (1920, 1080):
                            config.resolution = (800, 600)

                    if raise_volume_button.checkForInput(Menu_mouse_position):
                        config.volume += 1
                        if config.volume > 100:
                            config.volume = 100

                    if lowered_volume_button.checkForInput(Menu_mouse_position):
                        config.volume -= 1
                        if config.volume < 1:
                            config.volume = 0

                    if apply_button.checkForInput(Menu_mouse_position):
                        back_to_menu = True

                volume = font.render(f'{config.volume}', True, "#1c90ad")
                resolution_button = Button(None, (self.screen_rect.centerx, self.screen_rect.top + 200), f"{config.resolution}", font, menu_text_color, hover_text_color)

            if back_to_menu == True:
                break

            # update
            pygame.display.flip()