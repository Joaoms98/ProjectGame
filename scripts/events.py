import pygame,sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox
from services.EventService import EventService

class Events:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.clock = pygame.time.Clock()

    def run(self):
        # objects instances 
        dict_lang = lang.Language.set_lang(self, config.language)
        text_box = TextBox(self.screen, 10, pygame.font.Font("assets/fonts/alagard.ttf", 20),(500,500))
        event_service = EventService()
        event_response = event_service.takeEvent()

        # load background images
        event_background = pygame.image.load('assets/buttons/decision_button.png')
        
        # events text variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30)       

        # events text variables
        event_text_color = "#ff0000"
        hover_text_color = "White"
        decisio_button_image =  pygame.image.load('assets/buttons/decision_button.png')
        
        #load decision button
        decision_button_1 = Button(decisio_button_image, (450,500), "1",font, event_text_color,hover_text_color)
        decision_button_2 = Button(decisio_button_image, (580,500), "2", font, event_text_color, hover_text_color)

        #textbox
        text = event_response.message
        color = (255,0,0)

       
        while True:
            # set frames
            self.clock.tick(self.fps)    
            event_mouse_position = pygame.mouse.get_pos()
            
            # draw background
            self.screen.blit(event_background, (0, 0))


            for decisionbutton in [
                    decision_button_1,
                    decision_button_2]:
                    decisionbutton.changeColor(event_mouse_position)
                    decisionbutton.update(self.screen)
                    text_box.draw(text, color,(280,260))
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if decision_button_1.checkForInput(event_mouse_position):
                        print('fodase')
                    if decision_button_2.checkForInput(event_mouse_position):
                        print('fodase')
            
            # update
            pygame.display.flip()




