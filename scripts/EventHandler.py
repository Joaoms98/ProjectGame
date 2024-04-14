import pygame,sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.Textbox import TextBox


class EventHandler:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.clock = pygame.time.Clock()
    
    def run(self, allies , message, decision1_text, decision2_text = None):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)

        # background variables
        event_background_image = pygame.image.load('assets/popups/fogbuttonpopup.png')
        event_background_format = pygame.transform.scale(event_background_image, (700,250))

        # decision buttons variables
        decision_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        decision_button_image_format = pygame.transform.scale(decision_button_image,(150,50))
        decision = 0

        # common buttons variables
        font = pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 15)
        base_color = (0,255,0)
        hover_color = (255,0,0)

        # quit button variables
        # quit_button = Button(decision_button_image_format, (500,310), "Sair", font, base_color, hover_color)

        #text box variable
        text_box = TextBox(
            10, pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 20),(600,600), 
            message, (255,255,255), (290,135)
        )

        while True:
            # set frames
            self.clock.tick(self.fps)

            # take mouse position
            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(event_background_format, (160, 105))

            #draw text box
            text_box.updateTextAnimation(self.screen, message)

            #updated decision button
            if decision2_text == None:
                decision_button_1 = Button(decision_button_image_format, (500,325), decision1_text, font, base_color, hover_color)
                #draw decision button
                decision_button_1.changeColor(mouse_position)
                decision_button_1.update(self.screen)

            else :
                decision_button_1 = Button(decision_button_image_format, (400,325), decision1_text, font, base_color, hover_color)    
                decision_button_2 = Button(decision_button_image_format, (600,325), decision2_text, font, base_color, hover_color)
                #draw decision button
                for decision_button in [decision_button_1, decision_button_2]:
                    decision_button.changeColor(mouse_position)
                    decision_button.update(self.screen)
 
            #verify events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:                        
                    if decision_button_1.checkForInput(mouse_position):
                        text_box.animation_done = False
                        decision = 1
                    if decision2_text != None:    
                        if decision_button_2.checkForInput(mouse_position) :
                            text_box.animation_done = False
                            decision = 2

            # update
            pygame.display.flip()

            if decision != 0:
                break

        return decision




