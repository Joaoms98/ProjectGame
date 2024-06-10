import pygame, sys
import random
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.TextBox import TextBox
from services.DamageCalculateService import DamageCalculateService
from response.BattleResponse import BattleResponse
from utils.enums.SkillType import SkillType

class Arena:
    def __init__(self, screen, screen_rect, fps, resolution, allies, enemies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.enemies = enemies
        self.equipment = equipment
        self.clock = pygame.time.Clock()
        self.damage_calculate_service = DamageCalculateService()

    def run(self):
        pygame.mixer.stop()
        theme_music_sfx= pygame.mixer.Sound('assets/music/battle_music.mp3')
        theme_music_sfx_volume = (config.volume - 15) / 100
        theme_music_sfx.set_volume(theme_music_sfx_volume)
        theme_music_sfx.play()

        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        response = BattleResponse(
                    back_to_event = False
                )

        for character in self.enemies:
            character.picture = pygame.image.load(f'{character.picture}').convert()
            character.pictureSelected = pygame.image.load(f'{character.pictureSelected}').convert()
            character.pictureDead = pygame.image.load(f'{character.pictureDead}').convert()

        # background variables
        background = pygame.transform.scale(
            pygame.image.load('assets/background/Arena_Background.jpg').convert(),
            self.resolution
        )

        # create attributes text
        attributes_text = self.createAttributesText()

        # create picture buttons
        team_picture_buttons = self.createTeamPictureButtons()
        enemy_picture_buttons = self.createEnemyPictureButtons()
        potion_picture_button = self.createPotionButton()

        # prompt variables
        text_box = self.createTextPrompt()
        text_response = ""
        black_image = 'assets/background/black_image.jpg'
        prompt_surface = pygame.transform.scale(
            pygame.image.load(black_image).convert(),
            (0, 0)
        )

        # attack buttons
        attack_buttons = self.createAttackButtons(self.allies[0])

        # confirm button variables
        confirm_button_text_font = pygame.font.Font("assets/fonts/font.ttf", 15)
        confirm_button = Button(None, (500, 600), "Confirmar", confirm_button_text_font, (255,255,255), (255,255,0))

        player_turn = True
        allie_choice = None
        attack = None

        while True:
            # set frames
            self.clock.tick(self.fps)

            mouse_position = pygame.mouse.get_pos()
            response = self.verifyBattleEnd()
            self.verifyCharacterHp()

            if all(allie.hp <= 0 for allie in self.allies):
                text_response = "         Gamer Over!!!  Melhore da próxima vez "
                confirm_button = Button(None, (500, 600), "Fechar o jogo", confirm_button_text_font, (255,0,0), (255,255,0))
                player_turn = False

            # update team_picture_buttons
            # team_picture_buttons = self.createTeamPictureButtons()
            enemy_picture_buttons = self.createEnemyPictureButtons()

            # draw background
            self.screen.blit(background, (0, 0))

            # draw prompt
            self.screen.blit(prompt_surface, (178, 470))
            text_box.updateTextAnimation(self.screen, text_response)

            # draw attributes
            for attributes in attributes_text:
                attributes.update(self.screen)

            # draw allies
            for team_character_button in team_picture_buttons:
                team_character_button.update(self.screen)

            # draw enemies
            for enemy_picture_button in enemy_picture_buttons:
                enemy_picture_button.update(self.screen)

            # draw attack button and draw potion
            if allie_choice != None:
                for button in attack_buttons:
                    button.changeColor(mouse_position)
                    button.update(self.screen)
                    potion_picture_button.update(self.screen)

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
                        if all(allie.hp <= 0 for allie in self.allies):
                            pygame.quit()
                        if confirm_button.checkForInput(mouse_position):
                            text_box = self.createTextPrompt()
                            response = self.verifyBattleEnd()
                            team_picture_buttons = self.createTeamPictureButtons()
                            enemy_picture_buttons = self.createEnemyPictureButtons()
            
                            enemy_alive = [enemy for enemy in self.enemies if enemy.dead == False]
                            allie_alive = [allie for allie in self.allies if allie.dead == False]

                            if len(enemy_alive) > 0:
                                text_response = self.damage_calculate_service.AttackDamage(
                                    random.randint(0,2), random.choice(enemy_alive), 
                                    random.choice(allie_alive), self.enemies, self.allies
                                )

                            attack = None
                            player_turn = True

                    if player_turn == True: 
                        # check for input allies button
                        for i, team_character_button in enumerate([team_picture_buttons[0], team_picture_buttons[1], team_picture_buttons[2]]):
                            if team_character_button.checkForInput(mouse_position):
                                team_picture_buttons = self.createTeamPictureButtons(i)
                                enemy_picture_buttons = self.createEnemyPictureButtons()
                                allie_choice = self.allies[i]
                                attack_buttons = self.createAttackButtons(allie_choice)
                                potion_picture_button = self.createPotionButton()

                        # check for input attack button
                        for i, attack_button in enumerate([attack_buttons[0], attack_buttons[1], attack_buttons[2]]):
                            if attack_button.checkForInput(mouse_position):
                                attack = i

                        # check for input enemy button
                        for i, enemy_button in enumerate([enemy_picture_buttons[0], enemy_picture_buttons[1], enemy_picture_buttons[2]]):
                            if enemy_button.checkForInput(mouse_position):
                                text_response = self.damage_calculate_service.AttackDamage(
                                    attack, allie_choice, self.enemies[i],
                                    self.allies, self.enemies, self.equipment
                                )
                                text_box = self.createTextPrompt()
                                player_turn = False
                                allie_choice = None
                        # check for input potion button
                        if potion_picture_button.checkForInput(mouse_position):
                            text_response = self.damage_calculate_service.PotionHeal(allie_choice)
                            player_turn = False
                            allie_choice = None
                            attack = None

            if response.back_to_event == True:
                theme_music_sfx.stop()
                break

            # update
            pygame.display.flip()
        
        response.allies = self.allies
        return response

    def createAttackButtons(self, allie_choice):
        hit_text_font = pygame.font.Font("assets/fonts/font.ttf", 15)

        hit_button1 = Button(None, (500, 150), allie_choice.skills[0].name, hit_text_font, (255,255,255), (255,255,0))
        hit_button2 = Button(None, (500, 200), allie_choice.skills[1].name, hit_text_font, (255,255,255), (255,255,0))
        hit_button3 = Button(None, (500, 250), allie_choice.skills[2].name, hit_text_font, (255,255,255), (255,255,0))

        return [hit_button1, hit_button2, hit_button3]

    def createTeamPictureButtons(self, allie_choice = None):
        for allie in self.allies: 
            if allie.dead == True:
                allie.picture = allie.pictureDead

        image_character_list = [self.allies[0].picture, self.allies[1].picture, self.allies[2].picture]

        if allie_choice is not None and self.allies[allie_choice].dead is not True:
            image_character_list[allie_choice] = pygame.image.load(self.allies[allie_choice].pictureSelected)


        team_character_button_0 = Button(image_character_list[0], (85, 100), None , None, None, None)
        team_character_button_1 = Button(image_character_list[1], (85, 260), None , None, None, None)
        team_character_button_2 = Button(image_character_list[2], (85, 420), None , None, None, None)

        return [team_character_button_0, team_character_button_1, team_character_button_2]

    def createEnemyPictureButtons(self):
        for enemy in self.enemies: 
            if enemy.dead == True:
                enemy.picture = enemy.pictureDead

        # enemy button variables
        image_0 = self.enemies[0].picture
        image_1 = self.enemies[1].picture
        image_2 = self.enemies[2].picture
        enemy_character_button_0 = Button(image_0, (915, 100), None , None, None, None)
        enemy_character_button_1 = Button(image_1, (915, 260), None , None, None, None)
        enemy_character_button_2 = Button(image_2, (915, 420), None , None, None, None)

        return [enemy_character_button_0, enemy_character_button_1, enemy_character_button_2]

    def createTextPrompt(self):
        prompt_text_font = pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 20)
        prompt_text_color = (255,255,255)
        prompt_text_pos = (285, 520)
        prompt_text_size_rect = (600,600)
        prompt_text_font_size = 10

        return TextBox(prompt_text_font_size, prompt_text_font, prompt_text_size_rect, "", prompt_text_color, prompt_text_pos)
    
    def createAttributesText(self):
        font_size = 15
        font = pygame.font.SysFont("arial", 15)
        size_rect = (1000,700)
        hp_text_color = (255, 0, 0)
        mp_text_color = (0, 0, 255)

        # allies
        hp_allies_1 = TextBox(font_size, font, size_rect, f"Hp: {self.allies[0].hp}", hp_text_color, (192, 90))
        mp_allies_1 = TextBox(font_size, font, size_rect, f"Mp: {self.allies[0].mp}", mp_text_color, (192, 110))

        hp_allies_2 = TextBox(font_size, font, size_rect, f"Hp {self.allies[1].hp}", hp_text_color, (192, 240))
        mp_allies_2 = TextBox(font_size, font, size_rect, f"Mp {self.allies[1].mp}", mp_text_color, (192, 260))

        hp_allies_3 = TextBox(font_size, font, size_rect, f"Hp {self.allies[2].hp}", hp_text_color, (192, 400))
        mp_allies_3 = TextBox(font_size, font, size_rect, f"Mp {self.allies[2].mp}", mp_text_color, (192, 420))

        # enemies
        hp_enemy_1 = TextBox(font_size, font, size_rect, f"Hp: {self.enemies[0].hp}", hp_text_color, (774, 90))
        mp_enemy_1 = TextBox(font_size, font, size_rect, f"Mp: {self.enemies[0].mp}", mp_text_color, (774, 110))

        hp_enemy_2 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[1].hp}", hp_text_color, (773, 240))
        mp_enemy_2 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[1].mp}", mp_text_color, (773, 260))

        hp_enemy_3 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[2].hp}", hp_text_color, (772, 400))
        mp_enemy_3 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[2].mp}", mp_text_color, (772, 420))

        return [hp_allies_1, mp_allies_1, hp_allies_2, mp_allies_2, 
                hp_allies_3, mp_allies_3, hp_enemy_1, mp_enemy_1,
                hp_enemy_2, mp_enemy_2, hp_enemy_3, mp_enemy_3]

    def createPotionButton(self):
        potion_image = pygame.image.load('assets/status_icon/potion.png')
        potion_button = Button(potion_image, (500, 300), None , None, None, None)

        return potion_button

    def verifyCharacterHp(self):
        for allie in self.allies:
            if allie.hp <=0:
                allie.dead = True

        for enemy in self.enemies:
            if enemy.hp <=0:
                enemy.dead = True

    def verifyBattleEnd(self):
        if all(enemy.hp <= 0 for enemy in self.enemies):
            return BattleResponse(
                    back_to_event = True,
                )

        if all(enemy.hp <= 0 for enemy in self.enemies):
            return BattleResponse(
                    back_to_event = True,
                )

        return BattleResponse(
                    back_to_event = False,
                )