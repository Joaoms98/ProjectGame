from response.EventResponse import EventResponse
from response.BattleResponse import BattleResponse
from scripts.CharacterSelect import CharacterSelect
from objects.Skill import Skill
from utils.enums.SkillType import SkillType
from objects.Character import Character
from scripts.Arena import Arena
from scripts.EventHandler import EventHandler

class MapBEvents:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, allies, equipment)

    def zone1(self) -> EventResponse:
            message="Você encontra diversos caixões abertos,"\
                    "deixando visível os restos mortais daqueles que uma hora habitavam essas terras."\
                    "Em um canto do local estão alguns equipamentos de pesquisas, indicando que alguém estava"\
                    "a procura de algo no local. Ao verificar um caixão, um esqueleto segura um amuleto e você"\
                    "se pergunta se alguma vez já viu aquele símbolo."
            decision1="Interagir"
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 2:
                return [2, 3]

            faith_total = self.allies[0].faith + self.allies[1].faith + self.allies[2].faith
            self.equipment.faith = self.equipment.faith + 1

            if faith_total == 1:

                for allie in self.allies:
                    allie.hp = allie.hp - 1

                message= "Graças aos anos de estudos em teologia,"\
                        "você identifica que símbolo é dedicado ao deus"\
                        "da dor e da colheita de uma religião que a muito"\
                        "tempo foi extinta, sendo acusados de sacrificar"\
                        "humanos para crescimento de suas plantações. Com seu"\
                        "conhecimento você faz uma oferenda de sangue e cita"\
                        "uma reza para terra em troca do amuleto."
                decision1="Ave maria"
                decision2="Cruz credo"
                self.event_handler.run(self.allies, message, decision1, decision2)
            else:
                message= "Você não consegue identificar aquele símbolo mas mesmo assim decide "\
                        "pegar o amuleto. No momento em que você o toca, o corpo esquelético agarra "\
                        "sua mão e você salta para trás conseguindo se afastar e manter o amuleto em "\
                        "suas mãos, porém você nota que mais corpos se levantam mostrando que mesmo mortos "\
                        "eles estão dispostos a lutar."
                decision1="Que pena!"
                decision2="Droga!"
                decision = self.event_handler.run(self.allies, message, decision1, decision2)

                skills_test = [Skill("attackdirect", SkillType.DIRECT, 1, 1, 'str'), Skill("attackarea", SkillType.AREA, 1, 1, 'str'), Skill("attackheal", SkillType.HEAL, 1, 1, 'str')]

                enemy1 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
                enemy2 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
                enemy3 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonSTR(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonSTR(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

                arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
                battleResponse = arena.run()

                return EventResponse(
                    activity_zone_buttons = [2, 3],
                    disable_zone_buttons = [0]
                )