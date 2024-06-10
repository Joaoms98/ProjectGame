import pygame
from response.EventResponse import EventResponse
from response.BattleResponse import BattleResponse
from scripts.CharacterSelect import CharacterSelect
from objects.Inventory import Inventory
from objects.Skill import Skill
from utils.enums.SkillType import SkillType
from objects.Character import Character
from scripts.Arena import Arena
from scripts.EventHandler import EventHandler
from utils.DiceRow import DiceRow
import utils.Config as config

class MapCEvents:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, allies, equipment)

    # 1 - Fim do beta
    def zone1(self) -> EventResponse:
            message="Você adentra a uma pequena vila para encontrar o responsavel pela missão, mas a continuação dessa história irá ficar para o futuro"\

            decision1="Interagir"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)

            message= "Agradecemos por jogar nosso jogo ---- Equipe Open Heads ---- "\
            
            decision1="Fechar o Jogo"
            decision2=None
            self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = [0]
            )
