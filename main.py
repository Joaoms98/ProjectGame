import pygame
import utils.Config as config
from data.Seed import Seed
from scripts.MapA import MapA
from scripts.MapB import MapB
from scripts.MapC import MapC
from scripts.MainMenu import MainMenu
from scripts.CharacterSelect import CharacterSelect


while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('The Return of Fhajar')

    #seeds
    seed = Seed()
    data_seed = seed.alliesSeed()

    menu = MainMenu(screen, screen_rect, config.fps, config.resolution)
    menu.run()

    character_select = CharacterSelect(screen, screen_rect, config.fps, config.resolution, data_seed['allies'])
    team_selected = character_select.run()
    
    mapA = MapA(screen, screen_rect, config.fps, config.resolution, team_selected, data_seed['equipments'])
    mapA.run()

    mapB = MapB(screen, screen_rect, config.fps, config.resolution, team_selected, data_seed['equipments'])
    mapB.run()

    mapC = MapC(screen, screen_rect, config.fps, config.resolution, team_selected, data_seed['equipments'])
    mapC.run()
