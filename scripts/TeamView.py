import pygame, sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.TextBox import TextBox

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
        background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            self.resolution
        )

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
            self.screen.blit(background, (0, 0))

            #draw quit button
            quit_button.changeColor(mouse_position)
            quit_button.update(self.screen)

            # draw team
            self.createAttributeTextBox()

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

    def createAttributeTextBox(self):
        attribute_font_size = 15
        attributes_font = pygame.font.SysFont("arial", 15)
        attributes_text_color = "#c5cddf"
        attributes_size_rect = (1000,700)
        attribute_image = pygame.transform.scale(
                pygame.image.load('assets/portraits/portrait_test_1.jpeg').convert(),
                (30, 30)
            )
        
        allies_count = 0
        for character in self.allies:
            x = 125 + (300 * allies_count)

            self.screen.blit(pygame.image.load(character.picture), (x, 50))

            self.screen.blit(attribute_image, (x, 220))
            self.screen.blit(attribute_image, (x, 260))
            self.screen.blit(attribute_image, (x, 300))
            self.screen.blit(attribute_image, (x, 340))
            self.screen.blit(attribute_image, (x, 380))
            self.screen.blit(attribute_image, (x, 420))
            self.screen.blit(attribute_image, (x, 460))
            self.screen.blit(attribute_image, (x, 500))
            
            hp_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Hp: {character.hp} ", attributes_text_color, (x + 40, 225))
            mp_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Mp: {character.mp} ", attributes_text_color, (x + 40, 265))
            defense_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Defense: {character.defense} ", attributes_text_color, (x + 40, 305))
            dexterity_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Dexterity: {character.dexterity} ", attributes_text_color, (x + 40, 345))
            strength_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Strength: {character.strength} ", attributes_text_color, (x + 40, 385))
            intelligence_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"intelligence: {character.intelligence} ", attributes_text_color, (x + 40, 425))
            faith_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Faith: {character.faith} ", attributes_text_color, (x + 40, 465))
            charisma_text_box = TextBox(attribute_font_size, attributes_font, attributes_size_rect, f"Charisma: {character.charisma} ", attributes_text_color, (x + 40, 505))

            allies_count = allies_count + 1
        
            attributes_text_box = [hp_text_box, mp_text_box, defense_text_box, dexterity_text_box, strength_text_box, intelligence_text_box, faith_text_box, charisma_text_box]

            for text_box in attributes_text_box:
                text_box.update(self.screen)