from objects.Character  import Character
from objects.Skill import Skill
from objects.Equipment import Equipment
from objects.Inventory import Inventory
from utils.enums.SkillType import SkillType

class Seed:
    def alliesSeed(self):

        #Skills
        skills_warrior = [
            Skill("Cortar", SkillType.DIRECTD6, 2, 0, 'str', 'assets/music/sword.mp3'),
            Skill("Estocada Profunda", SkillType.DIRECTD12, 3, 5, 'str', 'assets/music/estocada_profunda.mp3'), 
            Skill("Grito de Guerra", SkillType.MANASTEALD20, 3, 10, 'str', 'assets/music/grito_de_guerra.mp3')
        ]
        skills_archer = [
            Skill("Disparo Rápido", SkillType.DIRECTD6, 4, 0, 'str', 'assets/music/arrow_impact.mp3'),
            Skill("Chuva de Flechas", SkillType.AREAD6, 3, 5, 'str', 'assets/music/arrow_rain.mp3'), 
            Skill("Flecha no Joelho", SkillType.DIRECTD20, 6, 15, 'str', 'assets/music/arrow_body_impact.mp3')
        ]

        skills_wizard = [
            Skill("Chicote de Fogo", SkillType.DIRECTD12, 3, 0, 'str', 'assets/music/fireball.mp3'), 
            Skill("Bola de Fogo", SkillType.AREAD6, 6, 5, 'str', 'assets/music/fireball.mp3'), 
            Skill("Meteóro", SkillType.AREAD20, 10, 20, 'str', 'assets/music/meteoro.mp3')
        ]

        skills_priest = [
            Skill("Toque de Luz", SkillType.DIRECTD12, 1, 0, 'str', 'assets/music/julgamento_toque_de_luz.mp3'), 
            Skill("Regeneração", SkillType.HEALD6, 1, 5, 'str', 'assets/music/healing.mp3'), 
            Skill("Surto de Vida", SkillType.HEALD12, 8, 15, 'str', 'assets/music/healing.mp3')
        ]

        skills_paladin = [
            Skill("Golpe Sagrado", SkillType.DIRECTD6, 3, 0, 'str', 'assets/music/corte.mp3'), 
            Skill("Julgamento", SkillType.DIRECTD12, 4, 5, 'str', 'assets/music/julgamento_toque_de_luz.mp3'), 
            Skill("Inspiração", SkillType.MANAREGEND12, 0, 15, 'str', 'assets/music/healing.mp3'),
        ]

        skills_mercenary = [
            Skill("Corte Curto", SkillType.DIRECTD6, 3, 0, 'str', 'assets/music/sword.mp3'), 
            Skill("Golpe Baixo", SkillType.DIRECTD6, 5, 5, 'str', 'assets/music/corte.mp3'),            
            Skill("Bomba de Veneno", SkillType.AREAD6, 2, 8, 'str', 'assets/music/meteoro.mp3')
        ]

        warrior_inventory = Inventory(1)
        archer_inventory = Inventory(1)
        wizard_inventory = Inventory(1)
        priest_inventory = Inventory(1)
        paladin_inventory = Inventory(1)
        mercenary_inventory = Inventory(1)

        # Characters
        warrior = Character(
            "Athedel", 
            'assets/portraits/Warrior-Athedel(Alive).png',
            'assets/portraits/Warrior-Athedel(Selected).png', 
            'assets/portraits/Warrior-Athedel(Dead).png', 
            70,35,5,10,1,1,3,5, 
            skills_warrior, 10, False, warrior_inventory
        )
        archer = Character(
            "Hilda",
            'assets/portraits/Archer-Hilda(Alive).png',
            'assets/portraits/Archer-Hilda(Selected).png', 
            'assets/portraits/Archer-Hilda(Dead).png', 
            40,60,0,3,6,3,4,9, 
            skills_archer, 10, False, archer_inventory
        )
        wizard = Character(
            "Agdrun",
            'assets/portraits/Wizard-Agudrun(Alive).png',
            'assets/portraits/Wizard-Agudrun(Selected).png', 
            'assets/portraits/Wizard-Agudrun(Dead).png', 
            35,70,1,2,10,4,5,3, 
            skills_wizard, 10, False, wizard_inventory
        )
        priest = Character(
            "Erinya",
            'assets/portraits/Priest-Erinya(Alive).png', 
            'assets/portraits/Priest-Erinya(Selected).png', 
            'assets/portraits/Priest-Erinya(Dead).png', 
            45,60,0,1,5,10,6,3, 
            skills_priest, 10, False, priest_inventory
        )
        paladin = Character(
            "Eder",
            'assets/portraits/DarkPaladin-Eder(Alive).png', 
            'assets/portraits/DarkPaladin-Eder(Selected).png', 
            'assets/portraits/DarkPaladin-Eder(Dead).png', 
            60,40,4,4,2,7,7,1, 
            skills_paladin, 10, False, paladin_inventory
        )
        mercenary = Character(
            "Harald",
            'assets/portraits/Mercenary-Harald(Alive).png', 
            'assets/portraits/Mercenary-Harald(Selected).png', 
            'assets/portraits/Mercenary-Harald(Dead).png', 
            50,50,2,7,4,3,3,6, 
            skills_mercenary, 10, False, mercenary_inventory
        )

        equipment = Equipment(0, 0, 0, 0, 0)

        return  {'allies': [warrior, archer, wizard, priest, paladin, mercenary] , 'equipments':  equipment}
        

        



