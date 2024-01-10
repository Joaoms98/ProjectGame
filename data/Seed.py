from objects.character  import Character

class Seed:
    def __int__(self):
        self.allies = None
    
    def alliesSeed(self):
        warrior = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,1,10,10,10,10,10)
        archer = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        wizard = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        cleric = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        paladin = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        mercenary = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)

    def enemySeed(self):
        #dex
        bandit_dex = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        animal_dex = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)

        #str
        bandit_str = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        animal_str = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)

        #int
        demon_int = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        
        #fai
        demon_faith = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)
        aberration_faith = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)

        #cha
        demon_lord_boss = Character("Fodase",'assets/portraits/portrait_test_1.jpeg',10,10,0,10,10,10,10,10)

        

        



