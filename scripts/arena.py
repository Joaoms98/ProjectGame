import pygame, sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.Textbox import TextBox

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

        # background variables
        background = pygame.transform.scale(
            pygame.image.load('assets/background/Untitled Map.jpg').convert(),
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
        black_image = 'assets/background/black_image.jpg'
        prompt = pygame.transform.scale(
            pygame.image.load(black_image).convert(),
            (650, 220)
        )

        font = pygame.font.Font("assets/fonts/font.ttf", 15)  
        
        hit_button1 = Button(None, (90, 500), "attack1", font, (255,0,0), (255,255,0))
        # hit_button2 = Button(None, (90, 550), "attack2", font, (0,0,0), (255,0,0))

        enemy_choice1 = Button(None, (900, 500), "enemie1", font, (255,0,0), (255,255,0))
        enemy_choice2 = Button(None, (900, 550), "enemie2", font, (255,0,0), (255,255,0))
        enemy_choice3 = Button(None, (900, 600), "enemie3", font, (255,0,0), (255,255,0))

        exit = Button(None, (500, 100), "exit", font, (0,0,0), (255,0,0))

        player_turn = True
        back_to_event = False

        while True:
            # set frames
            self.clock.tick(self.fps)

            mouse_position = pygame.mouse.get_pos()
            
            # draw background
            self.screen.blit(background, (0, 0))

            # draw prompt
            self.screen.blit(prompt, (178, 470))

            for attributes in attributes_text:
                attributes.update(self.screen)

            # draw allies
            allies_count = 0
            for character in self.allies:
                y = 20 + (151 * allies_count)
                self.screen.blit(character.picture, (15, y))
                allies_count = allies_count + 1

            # draw enemies
            enemies_count = 0
            for character in self.enemies:
                y = 20 + (151 * enemies_count)
                self.screen.blit(character.picture, (840, y))
                enemies_count = enemies_count + 1

            # draw attack button
            if player_turn == True:
                hit_button1.changeColor(mouse_position)
                hit_button1.update(self.screen)

                enemy_choice1.changeColor(mouse_position)
                enemy_choice1.update(self.screen)
                enemy_choice2.changeColor(mouse_position)
                enemy_choice2.update(self.screen)
                enemy_choice3.changeColor(mouse_position)
                enemy_choice3.update(self.screen)

            exit.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hit_button1.checkForInput(mouse_position):
                        print('hit1')
                        attack = 1

                    if player_turn == True:
                        if enemy_choice1.checkForInput(mouse_position):
                            enemy_choice = self.enemies[0]
                            self.hitButton(attack, enemy_choice)
                            player_turn = False
                        if enemy_choice2.checkForInput(mouse_position):
                            enemy_choice = self.enemies[1]
                            self.hitButton(attack, enemy_choice)
                            player_turn = False
                        if enemy_choice3.checkForInput(mouse_position):
                            enemy_choice = self.enemies[2]
                            self.hitButton(attack, enemy_choice)
                            player_turn = False

                    attributes_text = self.createAttributesText()

                if back_to_event == True:
                    break

            # update
            pygame.display.flip()

    def createAttributesText(self):
        font_size = 15
        font = pygame.font.SysFont("arial", 15)
        size_rect = (1000,700)
        hp_text_color = (255, 0, 0)
        mp_text_color = (0, 255, 0)

        #allies
        hp_allies_1 = TextBox(font_size, font, size_rect, f"Hp: {self.allies[0].hp}", hp_text_color, (180, 50))
        mp_allies_1 = TextBox(font_size, font, size_rect, f"Mp: {self.allies[0].mp}", mp_text_color, (180, 100))

        hp_allies_2 = TextBox(font_size, font, size_rect, f"Hp {self.allies[1].hp}", hp_text_color, (180, 200))
        mp_allies_2 = TextBox(font_size, font, size_rect, f"Mp {self.allies[1].mp}", mp_text_color, (180, 250))

        hp_allies_3 = TextBox(font_size, font, size_rect, f"Hp {self.allies[2].hp}", hp_text_color, (180, 350))
        mp_allies_3 = TextBox(font_size, font, size_rect, f"Mp {self.allies[2].mp}", mp_text_color, (180, 400))

        #enemies
        hp_enemy_1 = TextBox(font_size, font, size_rect, f"Hp: {self.enemies[0].hp}", hp_text_color, (780, 50))
        mp_enemy_1 = TextBox(font_size, font, size_rect, f"Mp: {self.enemies[0].mp}", mp_text_color, (780, 100))

        hp_enemy_2 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[1].hp}", hp_text_color, (780, 200))
        mp_enemy_2 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[1].mp}", mp_text_color, (780, 250))

        hp_enemy_3 = TextBox(font_size, font, size_rect, f"Hp {self.enemies[2].hp}", hp_text_color, (780, 350))
        mp_enemy_3 = TextBox(font_size, font, size_rect, f"Mp {self.enemies[2].mp}", mp_text_color, (780, 400))

        return [hp_allies_1, mp_allies_1, hp_allies_2, mp_allies_2, 
                hp_allies_3, mp_allies_3, hp_enemy_1, mp_enemy_1,
                hp_enemy_2, mp_enemy_2, hp_enemy_3, mp_enemy_3]

    def hitButton(self, attack, enemy):
        enemy.hp = enemy.hp - attack
        
    