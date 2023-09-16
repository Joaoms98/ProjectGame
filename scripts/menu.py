import pygame, sys
from utils.button import Button
from scripts.options import Options

class Menu:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def menu(self):
        # objects instances 
        options = Options(self.screen, self.screen_rect, self.fps, self.resolution)

        # load background images
        menu_background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

        # menu text variables
        font = pygame.font.Font("assets/fonts/font.ttf", 50)        
        menu_text = font.render("MAIN MENU", True, "#11ebeb")
        menu_text_rect = menu_text.get_rect(center=(self.screen_rect.centerx, 100))

        # menu button text variables
        menu_text_color = "#1c90ad"
        hover_text_color = "White"
        button = pygame.Rect(100, 100, 50, 50)
        image = pygame.image.load("assets/Play Rect.png")

        play_button = Button(image, (self.screen_rect.centerx, self.screen_rect.centery), "Play", font, menu_text_color, hover_text_color)
        options_button = Button(image, (self.screen_rect.centerx, self.screen_rect.centery + 120), "Opções", font, menu_text_color, hover_text_color)
        quit_button = Button(image, (self.screen_rect.centerx, self.screen_rect.centery + 240), "Sair", font, menu_text_color, hover_text_color)
        
        aply_changes_config = False
        
        while True:
            # set frames
            self.clock.tick(self.fps)

            Menu_mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(menu_background, (0, 0))

            # draw menu text
            self.screen.blit(menu_text, menu_text_rect)

            # draw button
            for button in [play_button, options_button, quit_button]:
                button.changeColor(Menu_mouse_position)
                button.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(Menu_mouse_position):
                        print('play')
                    if options_button.checkForInput(Menu_mouse_position):
                        options.options()
                        aply_changes_config = True
                    if quit_button.checkForInput(Menu_mouse_position):
                        pygame.quit()
                        sys.exit()

            if aply_changes_config == True:
                break

            # update
            pygame.display.flip()