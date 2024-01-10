import pygame,sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox
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
        text_box = TextBox(self.screen, 10, pygame.font.Font("assets/fonts/alagard.ttf", 20),(600,600))
        event_service = EventService(self.screen, self.screen_rect, self.fps, self.resolution)
        event_response = event_service.TakeEvent(eventId)

        # background variables
        event_background = pygame.image.load('assets/popups/fogbuttonpopup.png')
        event_background_format = pygame.transform.scale(event_background,(900,350))
        # buttons variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 15)
        decision_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        decision_button_image_format = pygame.transform.scale(decision_button_image,(150,50))
        
        base_color = (0,255,0)
        hover_color = (255,0,0)
        quit_button = Button(decision_button_image_format, (500,310), "Sair", font, base_color, hover_color)

        while True:
            # set frames
            self.clock.tick(self.fps)

            # take mouse position
            mouse_position = pygame.mouse.get_pos()

            #updated decision button
            decision_button_1 = Button(decision_button_image_format, (400,310), event_response.decision1, font, base_color, hover_color)
            decision_button_2 = Button(decision_button_image_format, (600,310), event_response.decision2 , font, base_color, hover_color)

            # draw background
            self.screen.blit(event_background_format, (50, 20))

            #draw text box
            text_box.draw(event_response.message, (255,255,255), (215,90))

            #draw quit button
            if event_response.completed == True:
                quit_button.changeColor(mouse_position)
                quit_button.update(self.screen)

            #draw decision button
            if event_response.completed == False:
                for decisionbutton in [decision_button_1, decision_button_2]:
                    decisionbutton.changeColor(mouse_position)
                    decisionbutton.update(self.screen)
 
            #verify events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event_response.completed == False:
                        if decision_button_1.checkForInput(mouse_position):
                            decision = 1
                            event_response = event_service.TakeEvent(eventId + "_2", decision, self.allies)
                        if decision_button_2.checkForInput(mouse_position):
                            decision = 2
                            event_response = event_service.TakeEvent(eventId + "_2", decision, self.allies)
                    if quit_button.checkForInput(mouse_position):
                        event_response.back = True

            # update
            pygame.display.flip()

            if event_response.back == True:
                break

        return event_response



