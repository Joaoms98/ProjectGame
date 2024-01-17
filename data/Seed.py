from objects.character  import Character

class Seed:
    def alliesSeed(self):
        warrior = Character("Athedel", 'assets/portraits/Warrior-Athedel(Alive).png', 'assets/portraits/Warrior-Athedel(Dead).png', 10,10,1,10,10,10,10,1)
        archer = Character("Hilda",'assets/portraits/Archer-Hilda(Alive).png', 'assets/portraits/Archer-Hilda(Dead).png', 10,10,0,10,10,10,10,2)
        wizard = Character("Agdrun",'assets/portraits/Wizard-Agudrun(Alive).png', 'assets/portraits/Wizard-Agudrun(Dead).png', 10,10,0,10,10,10,10,3)
        priest = Character("Erinya",'assets/portraits/Priest-Erinya(Alive).png', 'assets/portraits/Priest-Erinya(Dead).png', 10,10,0,10,10,10,10,4)
        paladin = Character("Eder",'assets/portraits/DarkPaladin-Eder(Alive).png', 'assets/portraits/DarkPaladin-Eder(Dead).png', 10,10,0,10,10,10,10,5)
        mercenary = Character("Harald",'assets/portraits/Mercenary-Harald(Alive).png', 'assets/portraits/Mercenary-Harald(Dead).png', 10,10,0,10,10,10,10,6)

        return [warrior, archer, wizard, priest, paladin, mercenary]

        

        



