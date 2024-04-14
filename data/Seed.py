from objects.Character  import Character
from objects.Skill import Skill
from objects.Equipment import Equipment
from utils.enums.SkillType import SkillType

class Seed:
    def alliesSeed(self):

        skills_test = [Skill("attackdirect", SkillType.DIRECTD6, 4, 1, 'str'), Skill("attackarea", SkillType.AREA, 2, 5, 'str'), Skill("attackheal", SkillType.HEAL, 2, 5, 'str')]
        skills_test2 = [Skill("attackdirect2", SkillType.DIRECTD12, 4, 1, 'str'), Skill("attackarea2", SkillType.AREA, 2, 5, 'str'), Skill("attackheal2", SkillType.HEAL, 2, 5, 'str')]

        warrior = Character("Athedel", 'assets/portraits/Warrior-Athedel(Alive).png', 'assets/portraits/Warrior-Athedel(Dead).png', 1,30,3,6,10,2,5,7, skills_test, 10, False)
        archer = Character("Hilda",'assets/portraits/Archer-Hilda(Alive).png', 'assets/portraits/Archer-Hilda(Dead).png', 1,65,0,10,10,10,10,2, skills_test2, 10, False)
        wizard = Character("Agdrun",'assets/portraits/Wizard-Agudrun(Alive).png', 'assets/portraits/Wizard-Agudrun(Dead).png', 55,80,0,10,10,10,10,3, skills_test, 10, False)
        priest = Character("Erinya",'assets/portraits/Priest-Erinya(Alive).png', 'assets/portraits/Priest-Erinya(Dead).png', 60,70,0,10,10,10,10,4, skills_test, 10, False)
        paladin = Character("Eder",'assets/portraits/DarkPaladin-Eder(Alive).png', 'assets/portraits/DarkPaladin-Eder(Dead).png', 80,60,2,10,10,10,10,5, skills_test, 10, False)
        mercenary = Character("Harald",'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 70,45,1,10,10,10,10,6, skills_test, 10, False)

        equipment = Equipment(0, 0, 0, 0, 0)

        return  {'allies': [warrior, archer, wizard, priest, paladin, mercenary] , 'equipments':  equipment}
        

        



