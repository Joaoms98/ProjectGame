from objects.Character  import Character
from objects.Skill import Skill
from utils.enums.SkillType import SkillType

class Seed:
    def alliesSeed(self):

        skills_test = [Skill("attackdirect", SkillType.DIRECT, 1, 1), Skill("attackarea", SkillType.AREA, 1, 1), Skill("attackheal", SkillType.HEAL, 1, 1)]
        skills_test2 = [Skill("attackdirect2", SkillType.DIRECT, 1, 1), Skill("attackarea2", SkillType.AREA, 1, 1), Skill("attackheal2", SkillType.HEAL, 1, 1)]
            
        warrior = Character("Athedel", 'assets/portraits/Warrior-Athedel(Alive).png', 'assets/portraits/Warrior-Athedel(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
        archer = Character("Hilda",'assets/portraits/Archer-Hilda(Alive).png', 'assets/portraits/Archer-Hilda(Dead).png', 10,10,0,10,10,10,10,2, skills_test2, 10, False)
        wizard = Character("Agdrun",'assets/portraits/Wizard-Agudrun(Alive).png', 'assets/portraits/Wizard-Agudrun(Dead).png', 10,10,0,10,10,10,10,3, skills_test, 10, False)
        priest = Character("Erinya",'assets/portraits/Priest-Erinya(Alive).png', 'assets/portraits/Priest-Erinya(Dead).png', 10,10,0,10,10,10,10,4, skills_test, 10, False)
        paladin = Character("Eder",'assets/portraits/DarkPaladin-Eder(Alive).png', 'assets/portraits/DarkPaladin-Eder(Dead).png', 10,10,0,10,10,10,10,5, skills_test, 10, False)
        mercenary = Character("Harald",'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 10,10,0,10,10,10,10,6, skills_test, 10, False)

        return [warrior, archer, wizard, priest, paladin, mercenary]

        

        



