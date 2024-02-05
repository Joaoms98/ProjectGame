import pygame, sys
import random
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.Textbox import TextBox
from services.DamageCalculateService import DamageCalculateService

class Arena:
    def __init__(self, screen, screen_rect, fps, resolution, allies, enemies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.enemies = enemies
        self.clock = pygame.time.Clock()

    def run(self):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        damage_calculate_service = DamageCalculateService(self.allies, self.enemies)

        # background variables
        background = pygame.transform.scale(
            pygame.image.load('assets/background/black_image.jpg').convert(),
            self.resolution
        )

        # format picture of allies and enemies
        for character in self.allies:
            character.picture = pygame.image.load(f'{character.picture}').convert()

        for character in self.enemies:
            character.picture = pygame.image.load(f'{character.picture}').convert()

        # create attributes text
        attributes_text = self.createAttributesText()

        # prompt variables
        black_image = 'assets/background/background_nuvens.jpg'
        prompt_text_font = pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 20)
        prompt_text_color = (255,255,255)
        text_response = ""
        prompt_text_pos = (300, 500)
        prompt_text_size_rect = (600,600)
        prompt_text_font_size = 10
        text_box = TextBox(prompt_text_font_size, prompt_text_font, prompt_text_size_rect, "", prompt_text_color, prompt_text_pos)
        prompt_surface = pygame.transform.scale(
            pygame.image.load(black_image).convert(),
            (650, 220)
        )

        # attack buttons
        attack_buttons = self.createAttackButtons(self.allies[0])

        # enemy button variables
        image_0 = self.enemies[0].picture
        image_1 = self.enemies[1].picture
        image_2 = self.enemies[2].picture
        enemy_character_button_0 = Button(image_0, (915, 100), None , None, None, None)
        enemy_character_button_1 = Button(image_1, (915, 260), None , None, None, None)
        enemy_character_button_2 = Button(image_2, (915, 420), None , None, None, None)

        # team button variables
        image_0 = self.allies[0].picture
        image_1 = self.allies[1].picture
        image_2 = self.allies[2].picture
        team_character_button_0 = Button(image_0, (85, 100), None , None, None, None)
        team_character_button_1 = Button(image_1, (85, 260), None , None, None, None)
        team_character_button_2 = Button(image_2, (85, 420), None , None, None, None)

        # confirm button variables
        confirm_button_text_font = pygame.font.Font("assets/fonts/font.ttf", 15)
        confirm_button = Button(None, (90, 500), "Confirm", confirm_button_text_font, (255,0,0), (255,255,0))

        player_turn = True
        back_to_event = False
        allie_choice = None

        while True:
            if all(allie.hp <= 0 for allie in self.allies):
                back_to_event = True

            if all(enemy.hp <= 0 for enemy in self.enemies):
                back_to_event = True

            # set frames
            self.clock.tick(self.fps)

            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(background, (0, 0))

            # draw prompt
            self.screen.blit(prompt_surface, (178, 470))
            text_box.updateTextAnimation(self.screen, text_response)

            # draw attributes
            for attributes in attributes_text:
                attributes.update(self.screen)

            # draw allies
            for enemy_picture_button in [team_character_button_0, team_character_button_1, team_character_button_2]:
                enemy_picture_button.update(self.screen)

            # draw enemies
            for enemy_picture_button in [enemy_character_button_0, enemy_character_button_1, enemy_character_button_2]:
                enemy_picture_button.update(self.screen)

            # draw attack button
            if allie_choice != None:
                for button in attack_buttons:
                    button.changeColor(mouse_position)
                    button.update(self.screen)

            # enemy hit
            if player_turn == False:
                confirm_button.changeColor(mouse_position)
                confirm_button.update(self.screen)

            # update attributes
            attributes_text = self.createAttributesText()

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_turn == False:
                        # check for input confirm button
                        if confirm_button.checkForInput(mouse_position):
                            player_turn = True
                            text_response = damage_calculate_service.EnemyAttackDamage(
                                random.randint(0,2), self.allies[random.randint(0,2)],  self.enemies[random.randint(0,2)]
                            )
                            text_box = TextBox(prompt_text_font_size, prompt_text_font, prompt_text_size_rect, "", 
                                               prompt_text_color, prompt_text_pos
                                            )

                    if player_turn == True: 
                        # check for input allies button
                        for i, team_character_button in enumerate([team_character_button_0, team_character_button_1, team_character_button_2]):
                            if team_character_button.checkForInput(mouse_position):
                                allie_choice = self.allies[i]
                                attack_buttons = self.createAttackButtons(allie_choice)

                        # check for input attack button
                        for i, attack_button in enumerate([attack_buttons[0], attack_buttons[1], attack_buttons[2]]):
                            if attack_button.checkForInput(mouse_position):
                                attack = i

                        # check for input enemy button
                        for i, enemy_button in enumerate([enemy_character_button_0, enemy_character_button_1, enemy_character_button_2]):
                            if enemy_button.checkForInput(mouse_position):
                                text_response = damage_calculate_service.PlayerAttackDamage(attack, self.enemies[i], allie_choice)
                                text_box = TextBox(prompt_text_font_size, prompt_text_font, prompt_text_size_rect, "", prompt_text_color, prompt_text_pos)
                                player_turn = False
                                allie_choice = None

            if back_to_event == True:
                break

            # update
            pygame.display.flip()

    def createAttackButtons(self, allie_choice):
        hit_text_font = pygame.font.Font("assets/fonts/font.ttf", 15)

        hit_button1 = Button(None, (90, 500), allie_choice.skills[0].name, hit_text_font, (255,0,0), (255,255,0))
        hit_button2 = Button(None, (90, 550), allie_choice.skills[1].name, hit_text_font, (255,0,0), (255,255,0))
        hit_button3 = Button(None, (90, 600), allie_choice.skills[2].name, hit_text_font, (255,0,0), (255,255,0))

        return [hit_button1, hit_button2, hit_button3]

    def createAttributesText(self):
        font_size = 15
        font = pygame.font.SysFont("arial", 15)
        size_rect = (1000,700)
        hp_text_color = (255, 0, 0)
        mp_text_color = (0, 255, 0)

        # allies
        hp_allies_1 = TextBox(font_size, font, size_rect, f"Hp: {self.allies[0].hp}", hp_text_color, (180, 50))
        mp_allies_1 = TextBox(font_size, font, size_rect, f"Mp: {self.allies[0].mp}", mp_text_color, (180, 100))

        hp_allies_2 = TextBox(font_size, font, size_rect, f"Hp {self.allies[1].hp}", hp_text_color, (180, 200))
        mp_allies_2 = TextBox(font_size, font, size_rect, f"Mp {self.allies[1].mp}", mp_text_color, (180, 250))

        hp_allies_3 = TextBox(font_size, font, size_rect, f"Hp {self.allies[2].hp}", hp_text_color, (180, 350))
        mp_allies_3 = TextBox(font_size, font, size_rect, f"Mp {self.allies[2].mp}", mp_text_color, (180, 400))

        # enemies
        hp_enemy_1 = TextBox(font_size, font, size_rect, f"Hp: {self.enemies[0].hp}", hp_text_color, (780, 50))
        mp_enemy_1 = TextBox(font_size, font, size_rect, f"Mp: {self.enemies[0].mp}", mp_text_color, (780, 100))

        hp_enemy_2 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[1].hp}", hp_text_color, (780, 200))
        mp_enemy_2 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[1].mp}", mp_text_color, (780, 250))

        hp_enemy_3 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[2].hp}", hp_text_color, (780, 350))
        mp_enemy_3 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[2].mp}", mp_text_color, (780, 400))

        return [hp_allies_1, mp_allies_1, hp_allies_2, mp_allies_2, 
                hp_allies_3, mp_allies_3, hp_enemy_1, mp_enemy_1,
                hp_enemy_2, mp_enemy_2, hp_enemy_3, mp_enemy_3]