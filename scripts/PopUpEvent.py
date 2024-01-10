import pygame,sys
import utils.language as lang
import utils.config as config
from utils.button import Button
from utils.textbox import TextBox
from services.EventService import EventService

class PopUpEvent:
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
        event_service = EventService(self.screen, self.screen_rect, self.fps, self.resolution)

        # background variables
        event_background = pygame.transform.scale(pygame.image.load('assets/buttons/decision_button.png').convert(),
            (700, 500)
        )

        # decision button variables
        font = pygame.font.Font("assets/fonts/alagard.ttf", 30)       
        decision_button_image =  pygame.image.load('assets/buttons/decision_button.png')

        decision_button_1 = Button(decision_button_image, (450,500), "decision1", font, (0,255,0), (255,0,0))
        decision_button_2 = Button(decision_button_image, (580,500), "decision2" , font, (0,255,0), (255,0,0))
       
        while True:
            # set frames
            self.clock.tick(self.fps)

            event_mouse_position = pygame.mouse.get_pos()
            
            # draw background
            self.screen.blit(event_background, (170, 70))

            for decisionbutton in [decision_button_1, decision_button_2]:
                    decisionbutton.changeColor(event_mouse_position)
                    decisionbutton.update(self.screen)
                    text_box.draw("take_event_response.message dshdjsh jshd sudhush dsh udsh dhsuihdsjhdushdsuhd dshui hshd uish djsui hdsjhd usihd jkshiudhsdhs uhds u shdh sdi ushj hsduk hsdj ", (255,255,255), (280,260))
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     # if decision_button_1.checkForInput(event_mouse_position):
                #     # if decision_button_2.checkForInput(event_mouse_position):

            # update
            pygame.display.flip()



