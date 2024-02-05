import pygame
import utils.Config as config
from data.Seed import Seed
from objects.Character import Character
from scripts.Arena import Arena
from scripts.MapA import MapA
from scripts.MapB import MapB
from scripts.MainMenu import Menu
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
    allies = seed.alliesSeed()

    # menu = Menu(screen, screen_rect, config.fps, config.resolution)
    # menu.menu()

    character_select = CharacterSelect(screen, screen_rect, config.fps, config.resolution, allies)
    team_selected = character_select.run()

    skills_test = [Skill("attackdirect", SkillType.DIRECT, 1, 1), Skill("attackarea", SkillType.AREA, 1, 1), Skill("attackheal", SkillType.HEAL, 1, 1)]

    enemy1 = Character("capiroto",'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
    enemy2 = Character("demonio", 'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
    enemy3 = Character("ditocujo",'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

    #arena = Arena(screen, screen_rect, config.fps, config.resolution, [allies[0], allies[1], allies[2]], [enemy1, enemy2, enemy3])
    #arena.run()

    #mapA = MapA(screen, screen_rect, config.fps, config.resolution, team_selected)
    #mapA.run()

    mapB = MapB(screen, screen_rect, config.fps, config.resolution, team_selected)
    mapB.run()