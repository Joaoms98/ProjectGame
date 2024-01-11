import pygame, sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox

class TeamView:
    def __init__(self, screen, screen_rect, fps, resolution, allies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.clock = pygame.time.Clock()

    def run(self):
        # Objects instances
        dict_lang = lang.Language.set_lang(self, config.language)

        # background variables
        campaing_background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            self.resolution
        )

        #atributes variables
        Atributtes_text_color = "#c5cddf"
        atributte_image = pygame.transform.scale(
                pygame.image.load('assets/portraits/portrait_test_1.jpeg').convert(),
                (30, 30)
            )

        Atributtes_text = TextBox(self.screen, 15, pygame.font.SysFont("arial", 15), (1000,700))

        #quit button variables
        quit_button_font = pygame.font.Font("assets/fonts/alagard.ttf", 15)
        quit_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        quit_button_image_format = pygame.transform.scale(quit_button_image,(150,50))
        quit_button_base_color = "#a9b0c7"
        quit_button_hover_color = "#ffffff"
        quit_button = Button(quit_button_image_format, (500,650), "Voltar", quit_button_font, quit_button_base_color, quit_button_hover_color)

        back = False

        while True:
            # set frames
            self.clock.tick(self.fps)
            
            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(campaing_background, (0, 0))

            #draw quit button
            quit_button.changeColor(mouse_position)
            quit_button.update(self.screen)

            # draw equipe
            allies_count = 0
            for character in self.allies:
                x = 125 + (300 * allies_count)

                self.screen.blit(pygame.image.load(character.picture), (x, 50))

                self.screen.blit(atributte_image, (x, 220))
                self.screen.blit(atributte_image, (x, 260))
                self.screen.blit(atributte_image, (x, 300))
                self.screen.blit(atributte_image, (x, 340))
                self.screen.blit(atributte_image, (x, 380))
                self.screen.blit(atributte_image, (x, 420))
                self.screen.blit(atributte_image, (x, 460))
                self.screen.blit(atributte_image, (x, 500))

                Atributtes_text.draw(f"Hp: {character.hp} ", Atributtes_text_color, (x + 40, 225))
                Atributtes_text.draw(f"Mp: {character.mp} ", Atributtes_text_color, (x + 40, 265))
                Atributtes_text.draw(f"Defense: {character.defense} ", Atributtes_text_color, (x + 40, 305))
                Atributtes_text.draw(f"Dexterity: {character.dexterity} ", Atributtes_text_color, (x + 40, 345))
                Atributtes_text.draw(f"Strength: {character.strength} ", Atributtes_text_color, (x + 40, 385))
                Atributtes_text.draw(f"intelligence: {character.intelligence} ", Atributtes_text_color, (x + 40, 425))
                Atributtes_text.draw(f"Faith: {character.faith} ", Atributtes_text_color, (x + 40, 465))
                Atributtes_text.draw(f"Charisma: {character.charisma} ", Atributtes_text_color, (x + 40, 505))
                
                allies_count = allies_count + 1

             # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkForInput(mouse_position):
                        back = True

            if back == True:
                break

            # update
            pygame.display.flip()

