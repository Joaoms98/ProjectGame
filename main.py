import pygame
import utils.config as config
from data.Seed import Seed
from objects.character import Character
from scripts.Arena import Arena
from scripts.MapA import MapA
from scripts.MapB import MapB
from scripts.MainMenu import MainMenu
from scripts.TeamView import TeamView
from scripts.CharacterSelect import CharacterSelect
from objects.Skill import Skill
from utils.enums.SkillType import SkillType

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')

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
