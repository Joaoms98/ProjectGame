import pygame
from scripts.campaing import Campaing
from scripts.menu import Menu
import utils.config as config

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')

    # campaing = Campaing(screen, screen_rect, config.fps, config.resolution)
    # campaing.campaing()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()