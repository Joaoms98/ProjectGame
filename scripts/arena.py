import pygame, sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.TextBox import TextBox

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
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
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

        # hit_button1 = Button(None, (90, 500), "attack1", font, (0,0,0), (255,0,0))
        # hit_button2 = Button(None, (90, 550), "attack2", font, (0,0,0), (255,0,0))

        # enemy_choice1 = Button(None, (900, 500), "enemie1", font, (0,0,0), (255,0,0))
        # enemy_choice2 = Button(None, (900, 550), "enemie2", font, (0,0,0), (255,0,0))
        # enemy_choice3 = Button(None, (900, 600), "enemie3", font, (0,0,0), (255,0,0))

        font = pygame.font.Font("assets/fonts/font.ttf", 15)  
        exit = Button(None, (500, 100), "exit", font, (0,0,0), (255,0,0))

        back_to_event = False

        while True:
            # set frames
            self.clock.tick(self.fps)

            mouse_position = pygame.mouse.get_pos()
            
            # draw background
            self.screen.blit(background, (0, 0))

            # draw prompt
            self.screen.blit(prompt, (178, 470))

            # draw allies
            allies_count = 0
            for character in self.allies:
                y = 20 + (151 * allies_count)
                self.screen.blit(character.picture, (15, y))
                allies_count = allies_count + 1
                attributes_text[0].updateText(self.screen, f'Hp: {character.hp}')
                attributes_text[1].updateText(self.screen, f'Mp: {character.mp}')

            # draw enemies
            enemies_count = 0
            for character in self.enemies:
                y = 20 + (151 * enemies_count)
                self.screen.blit(character.picture, (840, y))
                enemies_count = enemies_count + 1

            # # draw attack buttom
            # hit_button1.changeColor(mouse_position)
            # hit_button1.update(self.screen)
            # hit_button2.changeColor(mouse_position)
            # hit_button2.update(self.screen)

            # enemie_choice1.changeColor(mouse_position)
            # enemie_choice1.update(self.screen)
            # enemie_choice2.changeColor(mouse_position)
            # enemie_choice2.update(self.screen)
            # enemie_choice3.changeColor(mouse_position)
            # enemie_choice3.update(self.screen)

            exit.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if hit_button1.checkForInput(mouse_position):
                #         print('hit1')
                #         attack = 10 
                #     if hit_button2.checkForInput(mouse_position):
                #         attack = 20
                #     if enemie_choice1.checkForInput(mouse_position):
                #         enemie_choice = self.enemies[0]
                #         self.hitbutton(attack, enemie_choice)
                #     if enemie_choice2.checkForInput(mouse_position):
                #         enemie_choice = self.enemies[1]
                #         self.hitbutton(attack, enemie_choice)
                #     if enemie_choice3.checkForInput(mouse_position):
                #         enemie_choice = self.enemies[2]
                #         self.hitbutton(attack, enemie_choice)
                #     if exit.checkForInput(mouse_position):
                #         back_to_event = True

                if back_to_event == True:
                    break

            # update
            pygame.display.flip()

    def createAttributesText(self):
        font_size = 15
        font = pygame.font.SysFont("arial", 15)
        size_rect = (1000,700)
        hp_text_color = (255, 0, 0)

        hp_allies_1 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 170))
        mp_allies_1 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 180))

        hp_allies_2 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 170))
        mp_allies_2 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 180))

        hp_allies_3 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 170))
        mp_allies_3 = TextBox(font_size, font, size_rect, "Hp", hp_text_color, (600, 180))

        return [hp_allies_1, mp_allies_1, hp_allies_2, mp_allies_2, hp_allies_3, mp_allies_3]

    def hitButton(self, attack, enemie):
        enemie.life = enemie.life -attack
        
    