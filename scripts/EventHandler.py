import pygame,sys
import utils.Language as lang
import utils.Config as config
from utils.Button import Button
from utils.Textbox import TextBox
from services.EventService import EventService

class EventHandler:
    def __init__(self, screen, screen_rect, fps, resolution, allies):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.clock = pygame.time.Clock()

    def run(self, eventId):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        event_service = EventService(self.screen, self.screen_rect, self.fps, self.resolution)

        # background variables
        event_background_image = pygame.image.load('assets/popups/fogbuttonpopup.png')
        event_background_format = pygame.transform.scale(event_background_image, (700,250))

        # decision buttons variables
        decision_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        decision_button_image_format = pygame.transform.scale(decision_button_image,(150,50))

        # common buttons variables
        font = pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 15)
        base_color = (0,255,0)
        hover_color = (255,0,0)

        # quit button variables
        quit_button = Button(decision_button_image_format, (500,310), "Sair", font, base_color, hover_color)

        #takeEvent
        event_response = event_service.TakeEvent(eventId)

        #text box variable
        text_box = TextBox(10, pygame.font.Font("assets/fonts/MorrisRomanBlackAlt.ttf", 20),(600,600), event_response.message, (255,255,255), (215,90))

        while True:
            # set frames
            self.clock.tick(self.fps)

            # take mouse position
            mouse_position = pygame.mouse.get_pos()

            # draw background
            self.screen.blit(event_background_format, (50, 20))

            #draw text box
            text_box.updateTextAnimation(self.screen, event_response.message)

            #draw quit button
            if event_response.completed == True:
                quit_button.changeColor(mouse_position)
                quit_button.update(self.screen)

            #updated decision button
            decision_button_1 = Button(decision_button_image_format, (400,310), event_response.decision1, font, base_color, hover_color)
            decision_button_2 = Button(decision_button_image_format, (600,310), event_response.decision2 , font, base_color, hover_color)

            #draw decision button
            if event_response.completed == False:
                for decision_button in [decision_button_1, decision_button_2]:
                    decision_button.changeColor(mouse_position)
                    decision_button.update(self.screen)
 
            #verify events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event_response.completed == False:
                        if decision_button_1.checkForInput(mouse_position):
                            text_box.animation_done = False
                            decision = 1
                            event_response = event_service.TakeEvent(eventId + "_2", decision, self.allies)
                        if decision_button_2.checkForInput(mouse_position):
                            text_box.animation_done = False
                            decision = 2
                            event_response = event_service.TakeEvent(eventId + "_2", decision, self.allies)
                    if quit_button.checkForInput(mouse_position):
                        event_response.back = True

            # update
            pygame.display.flip()

            if event_response.back == True:
                break

        return event_response




