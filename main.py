import pygame
from data.Seed import Seed
from scripts.Map1 import Map1
from scripts.Map2 import Map2
from scripts.menu import Menu
from scripts.CharacterSelect import CharacterSelect
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
    allies = seed.alliesSeed()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()

    character_select = CharacterSelect(screen, screen_rect, config.fps, config.resolution, allies)
    team_selected = character_select.run()

    # map1 = Map1(screen, screen_rect, config.fps, config.resolution, team_selected)
    # map1.run()

    map2 = Map2(screen, screen_rect, config.fps, config.resolution, team_selected)
    map2.run()