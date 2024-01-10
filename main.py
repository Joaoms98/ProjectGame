import pygame
from scripts.Map1 import Map1
from scripts.arena import Arena
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

    # enemie1 = Character("Capiroto", player_picture, 100)
    # enemie2 = Character("demonio", player_picture, 100)
    # enemie3 = Character("ditocujo", player_picture, 100)

    # arena = Arena(screen, screen_rect, config.fps, config.resolution, (allie1, allie2, allie3), (enemie1, enemie2, enemie3))
    # arena.arena()

    map1 = Map1(screen, screen_rect, config.fps, config.resolution, [allie1, allie2, allie3])
    map1.run()

    # campaing = Campaing(screen, screen_rect, config.fps, config.resolution)
    # Campaing.run()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()