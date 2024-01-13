from objects.character  import Character

class Seed:
    def alliesSeed(self):
        warrior = Character("teste1", 'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,1,10,10,10,10,1)
        archer = Character("teste2",'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,0,10,10,10,10,2)
        wizard = Character("teste3",'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,0,10,10,10,10,3)
        cleric = Character("teste4",'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,0,10,10,10,10,4)
        paladin = Character("teste5",'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,0,10,10,10,10,5)
        mercenary = Character("teste6",'assets/portraits/Haguddrun(Wizard).png', 'assets/portraits/Haguddrun(Wizard)_dead.png', 10,10,0,10,10,10,10,6)

        return [warrior, archer, wizard, cleric, paladin, mercenary]

        

        



