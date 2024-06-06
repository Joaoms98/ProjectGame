import pygame, sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.Textbox import TextBox

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

        #attribute icons
        attribute_hp = pygame.image.load('assets\status_icon\StatusIcon-HP.png')
        attribute_mp = pygame.image.load('assets\status_icon\StatusIcon-MP.png')
        attribute_def =  pygame.image.load('assets\status_icon\StatusIcon-DF.png')
        attribute_dex = pygame.image.load('assets\status_icon\StatusIcon-DE.png')
        attribute_str = pygame.image.load('assets\status_icon\StatusIcon-ST.png')
        attribute_int = pygame.image.load('assets\status_icon\StatusIcon-IN.png')
        attribute_fai = pygame.image.load('assets\status_icon\StatusIcon-FA.png')
        attribute_cha = pygame.image.load('assets\status_icon\StatusIcon-CH.png')

        
        allies_count = 0
        for character in self.allies:
            x = 125 + (300 * allies_count)

            self.screen.blit(character.picture, (x, 50))

            self.screen.blit(attribute_hp, (x, 220))
            self.screen.blit(attribute_mp, (x, 260))
            self.screen.blit(attribute_def, (x, 300))
            self.screen.blit(attribute_dex, (x, 340))
            self.screen.blit(attribute_str, (x, 380))
            self.screen.blit(attribute_int, (x, 420))
            self.screen.blit(attribute_fai, (x, 460))
            self.screen.blit(attribute_cha, (x, 500))
            
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