from objects.character  import Character
from objects.Skill import Skill
from objects.Equipment import Equipment
from utils.enums.SkillType import SkillType

class Seed:
    def alliesSeed(self):

        #Skills
        skills_warrior = [
            Skill("Golpe De Lamina", SkillType.DIRECTD6, 2, 2, 'str'),
            Skill("Estocada Profunda", SkillType.DIRECTD6, 4, 5, 'str'), 
            Skill("Grito de Guerra", SkillType.MANASTEALD20, 0, 10, 'str')
        ]
        skills_archer = [
            Skill("Flecha Rápida", SkillType.DIRECTD6, 3, 2, 'str'),
            Skill("Chuva de Flechas", SkillType.AREAD6, 3, 5, 'str'), 
            Skill("Tiro no Joelho", SkillType.DIRECTD20, 5, 20, 'str')
        ]

        skills_wizard = [
            Skill("Raio Flamejante", SkillType.DIRECTD12, 1, 2, 'str'), 
            Skill("Bola De Fogo", SkillType.AREAD6, 6, 5, 'str'), 
            Skill("Meteoro", SkillType.AREAD20, 10, 20, 'str')
        ]

        skills_priest = [
            Skill("Ataque de Luz", SkillType.DIRECTD12, 1, 1, 'str'), 
            Skill("Regeneração", SkillType.HEALD6, 0, 5, 'str'), 
            Skill("Surto de Vida", SkillType.HEALD12, 5, 10, 'str')
        ]

        skills_paladin = [
            Skill("Golpe Sagrado", SkillType.DIRECTD6, 2, 1, 'str'), 
            Skill("Julgamento", SkillType.DIRECTD12, 3, 5, 'str'), 
            Skill("Inspiração", SkillType.MANAREGEND12, 0, 15, 'str'),
        ]

        skills_mercenary = [
            Skill("Julgamento", SkillType.DIRECTD6, 3, 1, 'str'), 
            Skill("Golpe Baixo", SkillType.DIRECTD6, 5, 5, 'str'),            
            Skill("Bomba", SkillType.AREAD6, 2, 8, 'str')
        ]

        # Characters
        warrior = Character(
            "Athedel", 
            'assets/portraits/Warrior-Athedel(Alive).png', 
            'assets/portraits/Warrior-Athedel(Dead).png', 
            70,30,5,10,1,1,3,5, 
            skills_warrior, 10, False
        )
        archer = Character(
            "Hilda",
            'assets/portraits/Archer-Hilda(Alive).png', 
            'assets/portraits/Archer-Hilda(Dead).png', 
            40,60,0,3,6,3,4,9, 
            skills_archer, 10, False
        )
        wizard = Character(
            "Agdrun",
            'assets/portraits/Wizard-Agudrun(Alive).png', 
            'assets/portraits/Wizard-Agudrun(Dead).png', 
            30,70,1,2,10,4,5,3, 
            skills_wizard, 10, False
        )
        priest = Character(
            "Erinya",'assets/portraits/Priest-Erinya(Alive).png', 
            'assets/portraits/Priest-Erinya(Dead).png', 
            40,60,0,1,5,10,6,3, 
            skills_priest, 10, False
        )
        paladin = Character(
            "Eder",
            'assets/portraits/DarkPaladin-Eder(Alive).png', 
            'assets/portraits/DarkPaladin-Eder(Dead).png', 
            60,40,4,4,2,7,7,1, 
            skills_paladin, 10, False
        )
        mercenary = Character(
            "Harald",
            'assets/portraits/Mercenary-Harald(Alive).png', 
            'assets/portraits/Mercenary-Harald(Dead).png', 
            50,50,2,7,4,3,3,6, 
            skills_mercenary, 10, False
        )

        equipment = Equipment(0, 0, 0, 0, 0)

        return  {'allies': [warrior, archer, wizard, priest, paladin, mercenary] , 'equipments':  equipment}
        

        



