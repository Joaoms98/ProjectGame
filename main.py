import pygame
from scripts.menu import Menu
import utils.config as config

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')

    menu = Menu(screen, screen_rect, config.fps, config.resolution)
    menu.menu()