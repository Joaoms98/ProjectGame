from objects.character  import Character

class Seed:
    def __int__(self):
        self.allies = None
        self.enemies = None

    def alliesSeed(self):
        warrior = Character("teste1",'assets/portraits/Haguddrun(Wizard).png',10,10,1,10,10,10,10,10)
        archer = Character("teste2",'assets/portraits/Haguddrun(Wizard).png',10,10,0,10,10,10,10,10)
        wizard = Character("teste3",'assets/portraits/Haguddrun(Wizard).png',10,10,0,10,10,10,10,10)
        cleric = Character("teste4",'assets/portraits/Haguddrun(Wizard).png',10,10,0,10,10,10,10,10)
        paladin = Character("teste5",'assets/portraits/Haguddrun(Wizard).png',10,10,0,10,10,10,10,10)
        mercenary = Character("teste6",'assets/portraits/Haguddrun(Wizard).png',10,10,0,10,10,10,10,10)

        allies = [warrior, archer, wizard, cleric, paladin, mercenary]
        self.allies = allies

        

        



