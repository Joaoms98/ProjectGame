import pygame
from scripts.Map1 import Map1
from scripts.Map2 import Map2
from scripts.menu import Menu
from objects.character import Character
import utils.config as config

while True:
    pygame.init()

    #set screen
    screen = pygame.display.set_mode(config.resolution)
    screen_rect = screen.get_rect()

    # set screen name
    pygame.display.set_caption('game')
    
    player_picture = 'assets/portraits/portrait_test_1.jpeg'
    allie1 = Character("José", player_picture, 100, 5)
    allie2 = Character("João", player_picture, 100, 5)
    allie3 = Character("Jesus", player_picture, 100, 4)

    map1 = Map1(screen, screen_rect, config.fps, config.resolution, [allie1, allie2, allie3])
    map1.run()

    map2 = Map2(screen, screen_rect, config.fps, config.resolution, [allie1, allie2, allie3])
    map1.run()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()