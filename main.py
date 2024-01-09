import pygame
from scripts.campaing import Campaing
from scripts.arena import Arena
from scripts.menu import Menu
import utils.config as config

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')

    arena = Arena(screen, screen_rect, config.fps, config.resolution)
    arena.arena()

    # campaing = Campaing(screen, screen_rect, config.fps, config.resolution)
    # campaing.campaing()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()