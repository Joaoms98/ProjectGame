import pygame, sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox

class Arena:
    def __init__(self, screen, screen_rect, fps, resolution, allies, enemies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.enemies = enemies
        self.clock = pygame.time.Clock()

    def arena(self):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)

        black_image = 'assets/background/black_image.jpg'

        ########## background ##############
        #format background image
        background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

        ######### allies and enemies #########
        Atributtes_text = TextBox(self.screen, 15, pygame.font.SysFont("arial", 15), (1000,700))

        #format picture of allies and enemies        
        for character in self.allies:
            character.picture = pygame.transform.scale(
                pygame.image.load(character.picture).convert(),
                (150, 150)
            )

        for character in self.enemies:
            character.picture = pygame.transform.scale(
                pygame.image.load(character.picture).convert(),
                (150, 150)
            )

        ############## prompt #############
        #format prompt image
        prompt = pygame.transform.scale(
            pygame.image.load(black_image).convert(),
            (650, 220)
        )

        font = pygame.font.Font("assets/fonts/font.ttf", 15)  
        hit_button1 = Button(None, (90, 500), "attack1", font, (0,0,0), (255,0,0))
        hit_button2 = Button(None, (90, 550), "attack2", font, (0,0,0), (255,0,0))

        enemie_choice1 = Button(None, (900, 500), "enemie1", font, (0,0,0), (255,0,0))
        enemie_choice2 = Button(None, (900, 550), "enemie2", font, (0,0,0), (255,0,0))
        enemie_choice3 = Button(None, (900, 600), "enemie3", font, (0,0,0), (255,0,0))

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
                Atributtes_text.draw(f"Life: {character.life} ", (255,0,0), (170, y + 20))

            # draw enemies
            enemies_count = 0
            for character in self.enemies:
                y = 20 + (151 * enemies_count)
                self.screen.blit(character.picture, (840, y))
                enemies_count = enemies_count + 1
                Atributtes_text.draw(f"Life: {character.life} ", (255,0,0), (780, y + 20))

            # draw attack buttom
            hit_button1.changeColor(mouse_position)
            hit_button1.update(self.screen)
            hit_button2.changeColor(mouse_position)
            hit_button2.update(self.screen)

            enemie_choice1.changeColor(mouse_position)
            enemie_choice1.update(self.screen)
            enemie_choice2.changeColor(mouse_position)
            enemie_choice2.update(self.screen)
            enemie_choice3.changeColor(mouse_position)
            enemie_choice3.update(self.screen)

            exit.update(self.screen)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hit_button1.checkForInput(mouse_position):
                        print('hit1')
                        attack = 10 
                    if hit_button2.checkForInput(mouse_position):
                        attack = 20
                    if enemie_choice1.checkForInput(mouse_position):
                        enemie_choice = self.enemies[0]
                        self.hitbutton(attack, enemie_choice)
                    if enemie_choice2.checkForInput(mouse_position):
                        enemie_choice = self.enemies[1]
                        self.hitbutton(attack, enemie_choice)
                    if enemie_choice3.checkForInput(mouse_position):
                        enemie_choice = self.enemies[2]
                        self.hitbutton(attack, enemie_choice)
                    if exit.checkForInput(mouse_position):
                        back_to_event = True

                if back_to_event == True:
                    break

            # update
            pygame.display.flip()

    def hitbutton(self, attack, enemie):
        enemie.life = enemie.life -attack
        
    