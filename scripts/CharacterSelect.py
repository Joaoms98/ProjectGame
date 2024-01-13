import pygame, sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox

class CharacterSelect:

    team_selected_index = []

    def __init__(self, screen, screen_rect, fps, resolution, allies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.clock = pygame.time.Clock()

    def run(self):
        back = False
        character_selected_index = None
    
        # Objects instances
        dict_lang = lang.Language.set_lang(self, config.language)

        # background variables
        background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            self.resolution
        )

        # confirm button variables
        confirm_button_font = pygame.font.Font("assets/fonts/alagard.ttf", 15)
        confirm_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        confirm_button_image_format = pygame.transform.scale(confirm_button_image,(150,50))
        confirm_button_base_color = "#a9b0c7"
        confirm_button_hover_color = "#ffffff"
        confirm_button = Button(confirm_button_image_format, (500,650), "Confirmar", confirm_button_font, confirm_button_base_color, confirm_button_hover_color)

        # create pictures button
        pictures_buttons = self.createCharacterPictureButton()

        # create attributes texts
        attribute_texts = self.createAttributes(character_selected_index)

        while True:
            # set frames
            self.clock.tick(self.fps)

            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(background, (0, 0))

            # draw character picture button
            for character_button in pictures_buttons:
                character_button.update(self.screen)

            # draw attributes
            if character_selected_index is not None:
                for attribute_text in attribute_texts:
                    attribute_text.update(self.screen)

            # draw confirm button
            if character_selected_index is not None:
                confirm_button.changeColor(mouse_position)
                confirm_button.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pictures_buttons[0].checkForInput(mouse_position) and not self.team_selected_index.__contains__(0):
                        character_selected_index = 0
                    if pictures_buttons[1].checkForInput(mouse_position) and not self.team_selected_index.__contains__(1):
                        character_selected_index = 1
                    if pictures_buttons[2].checkForInput(mouse_position) and not self.team_selected_index.__contains__(2):
                        character_selected_index = 2
                    if pictures_buttons[3].checkForInput(mouse_position) and not self.team_selected_index.__contains__(3):
                        character_selected_index = 3
                    if pictures_buttons[4].checkForInput(mouse_position) and not self.team_selected_index.__contains__(4):
                        character_selected_index = 4
                    if pictures_buttons[5].checkForInput(mouse_position) and not self.team_selected_index.__contains__(5):
                        character_selected_index = 5

                    attribute_texts = self.createAttributes(character_selected_index)

                    if character_selected_index is not None:
                        if confirm_button.checkForInput(mouse_position):

                            if not self.team_selected_index.__contains__(character_selected_index):
                                self.team_selected_index.append(character_selected_index)

                            pictures_buttons = self.createCharacterPictureButton()

                            for index in self.team_selected_index:
                                pictures_buttons[index].image = pygame.image.load(self.allies[index].pictureDead)

                            if len(self.team_selected_index) >= 3:
                                back = True
 
            if back == True:
                return [self.allies[self.team_selected_index[0]], self.allies[self.team_selected_index[1]], self.allies[self.team_selected_index[2]]]

            # update
            pygame.display.flip()

    def createAttributes(self, character_attributes_index: int = None):
        attributes_text_color = "#c5cddf"
        attributes_text_font = pygame.font.SysFont("arial", 20)
        attributes_size_rect = (1000,700)
        attributes_font_size = 15

        if character_attributes_index is not None:
            name_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"{self.allies[character_attributes_index].name}", attributes_text_color, (670, 25))
            hp_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Hp: {self.allies[character_attributes_index].hp}", attributes_text_color, (500, 100))
            mp_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Mp: {self.allies[character_attributes_index].mp}", attributes_text_color, (840, 100))
            defense_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Defense: {self.allies[character_attributes_index].defense}", attributes_text_color, (500, 175))
            dexterity_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Dexterity: {self.allies[character_attributes_index].dexterity}", attributes_text_color, (840, 175))
            strength_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Strength: {self.allies[character_attributes_index].strength}", attributes_text_color, (500, 250))
            intelligence_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Intelligence: {self.allies[character_attributes_index].intelligence}", attributes_text_color, (840, 250))
            faith_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Faith: {self.allies[character_attributes_index].faith}", attributes_text_color, (500, 325))
            charisma_text_box = TextBox(attributes_font_size, attributes_text_font, attributes_size_rect, f"Charisma: {self.allies[character_attributes_index].charisma}", attributes_text_color, (840, 325))

            return [name_text_box, hp_text_box, mp_text_box, defense_text_box, dexterity_text_box, strength_text_box, intelligence_text_box, faith_text_box, charisma_text_box]
    
    def createCharacterPictureButton(self):
        picture_character_0 = Button(pygame.image.load(self.allies[0].picture), (100,100), None , None, None, None)
        picture_character_1 = Button(pygame.image.load(self.allies[1].picture), (270,100), None , None, None, None)
        picture_character_2 = Button(pygame.image.load(self.allies[2].picture), (100,270), None , None, None, None)
        picture_character_3 = Button(pygame.image.load(self.allies[3].picture), (270,270), None , None, None, None)
        picture_character_4 = Button(pygame.image.load(self.allies[4].picture), (100,440), None , None, None, None)
        picture_character_5 = Button(pygame.image.load(self.allies[5].picture), (270,440), None , None, None, None)

        return [picture_character_0, picture_character_1, picture_character_2, picture_character_3, picture_character_4, picture_character_5]
