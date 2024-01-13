import pygame
from data.Seed import Seed
from objects.character import Character
from scripts.Arena import Arena
from scripts.Map1 import Map1
from scripts.Map2 import Map2
from scripts.MainMenu import Menu
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
    allies = seed.alliesSeed()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()

    # character_select = CharacterSelect(screen, screen_rect, config.fps, config.resolution, allies)
    # team_selected = character_select.run()

    enemy1 = Character("capiroto", 'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,1,10,10,10,10,1)
    enemy2 = Character("demonio", 'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,1,10,10,10,10,1)
    enemy3 = Character("ditocujo", 'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,1,10,10,10,10,1)

    arena = Arena(screen, screen_rect, config.fps, config.resolution, [allies[0], allies[1], allies[2]], [enemy1, enemy2, enemy3])
    arena.run()

    # map1 = Map1(screen, screen_rect, config.fps, config.resolution, team_selected)
    # map1.run()

    # map2 = Map2(screen, screen_rect, config.fps, config.resolution, team_selected)
    # map2.run()

