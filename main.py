import pygame
from data.Seed import Seed
from scripts.Map1 import Map1
from scripts.Map2 import Map2
from scripts.menu import Menu
from scripts.TeamView import TeamView
from objects.character import Character
import utils.config as config

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')
    
    #seeds
    seed = Seed()
    seed.alliesSeed()

    map1 = Map1(screen, screen_rect, config.fps, config.resolution, [seed.allies[0], seed.allies[1], seed.allies[2]])
    map1.run()

    # map2 = Map2(screen, screen_rect, config.fps, config.resolution, [warrior,archer,wizard])
    # map2.run()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()