from objects.Character  import Character
from objects.Skill import Skill
from objects.Equipment import Equipment
from objects.Inventory import Inventory
from utils.enums.SkillType import SkillType

class Seed:
    def alliesSeed(self):

        #Skills
        skills_warrior = [
            Skill("Cortar", SkillType.DIRECTD6, 2, 0, 'str'),
            Skill("Estocada Profunda", SkillType.DIRECTD6, 4, 5, 'str'), 
            Skill("Grito de Guerra", SkillType.MANASTEALD20, 0, 10, 'str')
        ]
        skills_archer = [
            Skill("Flecha Rápida", SkillType.DIRECTD6, 3, 0, 'str'),
            Skill("Chuva de Flechas", SkillType.AREAD6, 3, 5, 'str'), 
            Skill("Tiro no Joelho", SkillType.DIRECTD20, 5, 20, 'str')
        ]

        skills_wizard = [
            Skill("Chicote de Fogo", SkillType.DIRECTD12, 1, 0, 'str'), 
            Skill("Bola de Fogo", SkillType.AREAD6, 6, 5, 'str'), 
            Skill("Meteóro", SkillType.AREAD20, 10, 20, 'str')
        ]

        skills_priest = [
            Skill("Toque de Luz", SkillType.DIRECTD12, 1, 1, 'str'), 
            Skill("Regeneração", SkillType.HEALD6, 0, 5, 'str'), 
            Skill("Surto de Vida", SkillType.HEALD12, 5, 10, 'str')
        ]

        skills_paladin = [
            Skill("Golpe Sagrado", SkillType.DIRECTD6, 2, 1, 'str'), 
            Skill("Julgamento", SkillType.DIRECTD12, 3, 5, 'str'), 
            Skill("Inspiração", SkillType.MANAREGEND12, 0, 15, 'str'),
        ]

        skills_mercenary = [
            Skill("Corte Curto", SkillType.DIRECTD6, 3, 1, 'str'), 
            Skill("Golpe Baixo", SkillType.DIRECTD6, 5, 5, 'str'),            
            Skill("Bomba", SkillType.AREAD6, 2, 8, 'str')
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
            70,30,5,10,1,1,3,5, 
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
            30,70,1,2,10,4,5,3, 
            skills_wizard, 10, False, wizard_inventory
        )
        priest = Character(
            "Erinya",
            'assets/portraits/Priest-Erinya(Alive).png', 
            'assets/portraits/Priest-Erinya(Selected).png', 
            'assets/portraits/Priest-Erinya(Dead).png', 
            40,60,0,1,5,10,6,3, 
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
        

        



