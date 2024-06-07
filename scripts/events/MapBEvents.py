from response.EventResponse import EventResponse
from response.BattleResponse import BattleResponse
from scripts.CharacterSelect import CharacterSelect
from objects.Inventory import Inventory
from objects.Skill import Skill
from utils.enums.SkillType import SkillType
from objects.Character import Character
from scripts.Arena import Arena
from scripts.EventHandler import EventHandler
from utils.DiceRow import DiceRow

class MapBEvents:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, allies, equipment)

    # 1 - Caixões Abertos
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
                return EventResponse(
                    activity_zone_buttons = [],
                    disable_zone_buttons = []
                )

            roll = DiceRow.dice6()
            faith_total = self.allies[0].faith + self.allies[1].faith + self.allies[2].faith + roll
            self.equipment.faith = self.equipment.faith + 1

            if faith_total >= 12:

                for allie in self.allies:
                    allie.hp = allie.hp - 2

                message= f"Resultado({faith_total}) - Teste(12): "\
                        "Graças aos anos de estudos em teologia,"\
                        "você identifica que símbolo é dedicado ao deus"\
                        "da dor e da colheita de uma religião que a muito"\
                        "tempo foi extinta, sendo acusados de sacrificar"\
                        "humanos para crescimento de suas plantações. Com seu"\
                        "conhecimento você faz uma oferenda de sangue e cita"\
                        "uma reza para terra em troca do amuleto."
                        
                decision1="Sair"
                decision2=None
                self.event_handler.run(self.allies, message, decision1, decision2)
            
            else:
                message= f"Resultado({faith_total}) - Teste(12): "\
                        "Você não consegue identificar aquele símbolo, mas mesmo assim decide "\
                        "pegar o amuleto. No momento em que você o toca, o corpo esquelético agarra "\
                        "sua mão e você salta para trás conseguindo se afastar e manter o amuleto em "\
                        "suas mãos, porém você nota que mais corpos se levantam mostrando que mesmo mortos "\
                        "eles estão dispostos a lutar."
                
                decision1="Enfrenta-los"
                decision2=None
                decision = self.event_handler.run(self.allies, message, decision1, decision2)
   
                skills_Skeleton_Dex = [Skill("Disparo Rápido", SkillType.DIRECTD6, 2, 0, 'str'), Skill("Chuva de Flechas", SkillType.DIRECTD6, 2, 10, 'str'), Skill("Flecha no Joelho", SkillType.DIRECTD12, 2, 20, 'str')]
                skills_Skeleton_Int = [Skill("Lança Sombria", SkillType.DIRECTD6, 1, 0, 'str'), Skill("Mísseis Mágico", SkillType.AREAD6, 3, 6, 'str'), Skill("Reconstrução", SkillType.HEALD6, 3, 10, 'str')]
                skills_Skeleton_Str = [Skill("Esmagar Leve", SkillType.DIRECTD6, 1, 0, 'str'), Skill("Esmagar Pesado", SkillType.DIRECTD6, 2, 5, 'str'), Skill("Provocar", SkillType.MANASTEALD6, 0, 10, 'str')]
                
                common_inventory = Inventory(0)
            
                enemy1 = Character("Esqueleto Arqueiro",'assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png','assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png','assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png',24,30,1,0,0,0,0,0,skills_Skeleton_Dex,10,False,common_inventory)
                enemy2 = Character("Esqueleto Mago",'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Dead).png', 20,60,0,0,0,0,0,0, skills_Skeleton_Int, 10, False, common_inventory)
                enemy3 = Character("Esqueleto Guerreiro",'assets/portraits/Enemies/Skeleton/SkeletonSTR(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonSTR(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonSTR(Dead).png', 40,10,0,0,0,0,0,0, skills_Skeleton_Str, 10, False, common_inventory)

                arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
                battleResponse = arena.run()

            return EventResponse(
                activity_zone_buttons = [2, 3],
                disable_zone_buttons = [0]
            )

    # 2 - Oferenda Estranha
    def zone2(self) -> EventResponse:
            message="Próximo ao fluxo de água, há algumas velas em algo que parece ser uma oferenda "\
                    ". Você se pergunta por que e para que serve essa oferenda"
            decision1="Destruir a oferenda "
            decision2="Jogar a oferenda na água"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:

                message="Você decide destruir a oferenda, porém nada acontece. Talvez seja melhor assim."
                decision1="Sair"
                decision2=None

                decision = self.event_handler.run(self.allies, message, decision1, decision2)

                return EventResponse(
                    activity_zone_buttons = [2],
                    disable_zone_buttons = [1]
                )

            message="Você decide jogar a oferenda na água, após alguns instantes um grupo de afogados aparecem "\
                    "mostrando toda sua fúria. Você percebe que não foi a melhor decisão."
            decision1="Enfrenta-los"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_drowned_Dex = [Skill("Arranhar", SkillType.DIRECTD6, 4, 0, 'str'), Skill("Garras Afiadas", SkillType.DIRECTD12, 2, 10, 'str'), Skill("Grito Atordoante", SkillType.MANASTEALD6, 1, 15, 'str')]
            skills_drowned_Int = [Skill("Cuspir Vômito", SkillType.DIRECTD6, 3, 0, 'str'), Skill("Regeneração", SkillType.HEALD12, 3, 10, 'str'), Skill("Grito Atordoante", SkillType.MANASTEALD6, 2, 15, 'str')]
            
            common_inventory = Inventory(0)
            
            enemy1 = Character("Afogado Caçador",'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Dead).png', 40,30,3,0,0,0,0,0, skills_drowned_Dex, 10, False, common_inventory)
            enemy2 = Character("Afogado Ancião",'assets/portraits/Enemies/Drowned/DrownedMonsterINT(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterINT(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterINT(Dead).png', 25,50,2,0,0,0,0,0, skills_drowned_Int, 10, False, common_inventory)
            enemy3 = Character("Afogado Caçador",'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Dead).png', 40,30,3,0,0,0,0,0, skills_drowned_Dex, 10, False, common_inventory)


            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()

            return EventResponse(
                activity_zone_buttons = [2],
                disable_zone_buttons = [1]
            )

    # 3 - Plantação de cogumelos
    def zone3(self) -> EventResponse:
        message="Você encontra um local com diversos cogumelos e percebe que alguém se dedicou "\
                "a cuidar desse lugar. Talvez há algo que você possa pegar, mas tem dificuldade em "\
                "identificar qual cogumelo levar."
                
        decision1="Vasculhar"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        intelligence_total = self.allies[0].intelligence + self.allies[1].intelligence + self.allies[2].intelligence + roll

        if intelligence_total >= 15:
            message= f"Resultado({intelligence_total}) - Teste(12/15): "\
                "Ao vasculhar, você encontra alguns cogumelos da realeza, conhecidos por "\
                "fortalecer e recarregar a energia daqueles que o ingerem. "\
                "(Todos ganham + 25 vida e + 30 de mana)"
            decision1="Sair"
            decision2=None

            for allie in self.allies:
                allie.hp  = allie.hp + 25
                allie.mp = allie.mp + 30

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )

        elif intelligence_total >=  12:
            message=f"Resultado({intelligence_total}) - Teste(12/15): "\
                    "Após vasculhar diversas vezes, você reconhece apenas um cogumelo e decide evitar os outros "\
                    "que você não reconhece."\
                    "(Todos ganham + 15 vida)"
            
            for allie in self.allies:
                allie.hp  = allie.hp + 15        
            
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )
        else:
            message=    f"Resultado({intelligence_total}) - Teste(12/15): "\
            "Você não consegue reconhecer nenhum e decide evitar ingerir algo que não conhece."
            
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )

    # 4 - Ninho de aranhas mutantes
    def zone4(self) -> EventResponse:
        message="Uma longa passagem estreita está coberta de ovos abertos de aranhas mutantes, é "\
                "possível avistar alguns exploradores que não tiverem sorte e acabaram enrolados "\
                "por teias. Você acaba notando que os cadáveres morreram recentemente e seus "\
                "equipamentos estão em um bom estado, mas sabe que não será fácil removê-los "\
                "das teias."
                
        decision1="Remover"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        roll = DiceRow.dice6()
        strength_total = self.allies[0].strength + self.allies[1].strength + self.allies[2].strength + roll

        if strength_total >= 15:
            message=    f"Resultado({strength_total}) - Teste(15): "\
                    "Você consegue usar sua força para cortar os fios grossos de teias sem dificuldade, "\
                    "deixando os cadáveres acessíveis. Ao coletar os equipamentos, você nota que na "\
                    "armadura de um explorador está o símbolo do reino de Karadur e se pergunta por "\
                    "que um soldado do rei estaria nesse local. "
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

 #           for allie in self.allies:
#                allie.defense  = allie.defense + 1

        else: 
            message=f"Resultado({strength_total}) - Teste(15): "\
                    "Mesmo usando sua força e técnica você não consegue romper os fios de teias, após "\
                    "desistir e olhar por alguns segundos para o cadáver você nota que em sua "\
                    "armadura está o símbolo do reino de Karadur e se pergunta por que um soldado do    "\
                    "rei estaria nesse local. "
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [2, 4],
            disable_zone_buttons = [3]
        )

    # 5 - Aranhas no antigo acampamento 
    def zone5(self) -> EventResponse:
        message="Ao chegar próximo do local você nota que há muitos exploradores mortos, presos "\
                "em teias e outros sem parte de seu corpo. Você se pergunta se é uma boa ideia "\
                "chegar perto do antigo acampamento. "
        decision1="Interagir "
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        message="Você decide passar pelo antigo acampamento mesmo sabendo do perigo "\
        "iminente das aranhas. O acampamento está todo destruído e nada pode ser "\
        "reaproveitado. Após alguns olhares em volta você percebe que não está sozinho e "\
        "terá que se defender."
        
        decision1="Lutar"
        decision2=None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        skills_spider_Dex= [Skill("Soltar Teias", SkillType.DIRECTD6, 3, 0, 'str'), Skill("Emboscar", SkillType.DIRECTD6, 5, 5, 'str'), Skill("Presas Venenosas", SkillType.DIRECTD12, 3, 10, 'str')]
        skills_spider_Int = [Skill("Soltar Teias", SkillType.DIRECTD6, 2, 1, 'str'), Skill("Guiar Filhotes", SkillType.AREAD6, 6, 5, 'str'), Skill("Cuspir Veneno", SkillType.AREAD12, 4, 10, 'str')]
        
        common_inventory = Inventory(0)
        
        enemy1 = Character("Aranha Armadilheira",'assets/portraits/Enemies/Spider/SpiderDEX(Alive).png','assets/portraits/Enemies/Spider/SpiderDEX(Alive).png', 'assets/portraits/Enemies/Spider/SpiderDEX(Dead).png', 38,15,2,0,0,0,0,0, skills_spider_Dex, 10, False, common_inventory)
        enemy2 = Character("Aranha Cuspideira",'assets/portraits/Enemies/Spider/SpiderINT(Alive).png', 'assets/portraits/Enemies/Spider/SpiderINT(Alive).png', 'assets/portraits/Enemies/Spider/SpiderINT(Dead).png', 30,40,1,0,0,0,0,0, skills_spider_Int, 10, False, common_inventory)
        enemy3 = Character("Aranha Armadilheira",'assets/portraits/Enemies/Spider/SpiderDEX(Alive).png','assets/portraits/Enemies/Spider/SpiderDEX(Alive).png', 'assets/portraits/Enemies/Spider/SpiderDEX(Dead).png', 38,15,2,0,0,0,0,0, skills_spider_Dex, 10, False, common_inventory)

        arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
        battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [7],
            disable_zone_buttons = [4]
        )

    # 6 - Caminhos escuros
    def zone6(self) -> EventResponse:
        message="A sua frente está um caminho apertado e escuro onde nem mesmo uma tacho será "\
                "de grande ajuda, após encarar a escuridão por um tempo você consegue ouvir "\
                "passos pesados ecoando pela passagem. Você decide que não é bom seguir esse "\
                "caminho."
                
        decision1="Prosseguir"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        return EventResponse(
            activity_zone_buttons = [6, 8],
            disable_zone_buttons = [5]
        )

    # 7 - Slimes
    def zone7(self) -> EventResponse:
        message="Ao olhar de longe, você percebe que há um amontoado de gosmas verdes entre seu "\
                "caminho e nunca viu algo desse tipo antes, se perguntando de onde essas coisas "\
                "surgiram."
                
        decision1="Interagir"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        message="Ao se aproximar das gosmas é possível sentir um cheiro de podridão e morte, "\
                "elas se separam em grupos e segue  em sua direção consumindo todos os restos "\
                "mortais que estão no local. "
        
        decision1="Lutar"
        decision2=None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        skills_Slime = [Skill("Engolir", SkillType.DIRECTD6, 5, 0, 'str'), Skill("Regeneração", SkillType.HEALD20, 10, 10, 'str'), Skill("Regeneração Maior", SkillType.HEALD20, 15, 20, 'str')]
        common_inventory = Inventory(0)
        
        enemy1 = Character("Slime",'assets/portraits/Enemies/Slime/Slime(Alive).png','assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 60,20,0,0,0,0,0,0, skills_Slime, 10, False, common_inventory)
        enemy2 = Character("Slime",'assets/portraits/Enemies/Slime/Slime(Alive).png','assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 60,20,0,0,0,0,0,0, skills_Slime, 10, False, common_inventory)
        enemy3 = Character("Slime",'assets/portraits/Enemies/Slime/Slime(Alive).png','assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 60,20,0,0,0,0,0,0, skills_Slime, 10, False, common_inventory)
        

        arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
        battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [11],
            disable_zone_buttons = [6]
        )
    
    # 8 - Barricada de madeira
    def zone8(self) -> EventResponse:
        message="Uma grande barreira de madeira improvisada foi montada aqui impedindo que algo "\
                "ou alguém passe, após analisar a estrutura você percebe que com uma boa "\
                "pancada é possível abrir uma passagem."
        
        decision1="Interagir"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        roll = DiceRow.dice6()
        strength_total = self.allies[0].strength + self.allies[1].strength + self.allies[2].strength + roll
        
        

        if strength_total >= 18:

            message= f"Resultado({strength_total}) - Teste(15):  "\
                    "Com uma boa pancada na estrutura você consegue derrubar a pilha de móveis "\
                    "improvisados para impedir o caminho, percebendo que qualquer monstro desse "\
                    "local poderia fazer o mesmo."
                    
            decision1="Prosseguir"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [14],
                disable_zone_buttons = [7]
            )

        message=f"Resultado({strength_total}) - Teste(15): "\
                "Mesmo com sua força os móveis e tábuas improvisadas ainda permanecem em pé, "\
                "você acaba se cansando e decide que é melhor encontrar outro caminho."
        
        decision1="Sair"
        decision2=None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

    # 9 - Inscrições na parede
    def zone9(self) -> EventResponse:
        message="Você encontra os restos mortais de dois exploradores, um deles segura uma faca "\
                "com a ponta desgastada por mau uso. Na parede próxima aos exploradores você "\
                "percebe que possui diversas inscrições, analisando você tenta entender o que elas "\
                "transmitem."
        decision1="Investigar"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        intelligence_total = self.allies[0].intelligence + self.allies[1].intelligence + self.allies[2].intelligence + roll

        if intelligence_total >= 12:
            
            message=f"Resultado({intelligence_total}) - Teste(12): "\
                    "As inscrições citam um conto antigo que pertence às terras do Céu Vermelho, "\
                    "citando o amor de um casal que se entregaram ao deus do fogo para "\
                    "permanecerem unidos e combater o mal no pós vida. Você se sente inspirado, mas "\
                    "logo percebe que os exploradores são um casal e infelizmente perderam a vida "\
                    "nesse local."
            
            decision1="Prosseguir"
            decision2=None
            decision = self.event_handler.run(self.allies, message, decision1, decision2)
        else:
            message=f"Resultado({intelligence_total}) - Teste(12): "\
                    "Você não consegue identificar o que as inscrições passam, mas sabe que antes de "\
                    "morrerem aqueles exploradores tentaram transmitir algo para o mundo."
            decision1="Sair"
            decision2=None
            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [9],
            disable_zone_buttons = [8]
        )
    
    # 10 - Homem preso
    def zone10(self) -> EventResponse:
        message="Você avista uma cela e dentro dela há um homem sentado,"\
                "ele susurra e entra pânico ao te ver, ele diz “Por "\
                "favor eu já sofri muito, acabe comigo de uma vez”. Você se aproxima da cela"\
                "tentando acalma-lo, o homem se aproxima de você."
        decision1="Ajuda-lo"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        charisma_total = self.allies[0].charisma + self.allies[1].charisma + self.allies[2].charisma + roll

        if charisma_total >= 18:
            message=f"Resultado({charisma_total}) - Teste(18): "\
                    "“Você não está com Voslok?” com uma expressão de esperança ele se aproxima da "\
                    "grade, “Você deve acabar com ele, aquele desgraçado me prendeu aqui."\
                    "Ele está no final do corredor com aquele cadaver”. Ele aponta para o final do corredor"\
                    "enquanto você o liberta, ele lhe agradece e foge para saida da caverna."
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)
        else: 
            message=f"Resultado({charisma_total}) - Teste(18): "\
                    "“Você… Você não devia estar aqui, todos irão morrer, aquele… aquele maldito "\
                    "cadaver”, o homem com tamanha destreza alcança a faca em sua cintura e "\
                    "rapidamente corta a garganta. Você apenas assiste aquele pobre "\
                    "homem morrer."
            
            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [10],
            disable_zone_buttons = [9]
        )
    
    # 11 - Suprimentos
    def zone11(self) -> EventResponse:
        message="A sala está cheia de prateleiras com diversas poções e alimentos que poderiam durar meses, porém alguns deles já não estão "\
        "seguros devido ao tempo, você pondera se alguma poção pode ser útil"

        decision1="Analisar poções"
        decision2="Seguir seu caminho"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:

            message="Você decide que é melhor não arriscar e segue seu caminho"

            decision1="Analisar poções"
            decision2="Seguir seu caminho"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)


            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        
        roll = DiceRow.dice6()
        intelligence_total = self.allies[0].intelligence + self.allies[1].intelligence + self.allies[2].intelligence + roll
        
        if intelligence_total >= 12:

            message=f"Resultado({intelligence_total}) - Teste(12): "\
                    "Você encontra algumas poções em bom estado e aproveita para bebe-las, "\
                    "sentindo revigorado você se prepara para o que vier."\
                    "(Todos os aliados ganham +30 vida e +30 mana.)"

            for allie in self.allies:
                allie.hp = allie.hp + 30
                allie.mp = allie.mp + 30
                
            decision1="Prosseguir"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [15],
                disable_zone_buttons = [10]
            )
        
        message=f"Resultado({intelligence_total}) - Teste(12): "\
                "Você não recohece as poções, mas decide se arriscar consumindo uma poção que lhe "\
                "chamou atenção, porém essa poção lhe faz sentir mal "\
                "(Todos os aliados perdem -25 vida e -25 mana.)"

        for allie in self.allies:
            allie.hp = allie.hp - 25
            allie.mp = allie.mp - 25

        decision1="Prosseguir"
        decision2=None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [15],
            disable_zone_buttons = [10]
        )

    # 12 - Resto mortais   
    def zone12(self) -> EventResponse:
        message="A sala está repleta de esqueletos e recentes cadáveres que estão no processo de decomposição,"\
        "com tanta morte e desespero você sente o peso das almas daqueles que tiveram um fim trágico"
        
        decision1="Rezar para os mortos"
        decision2="Ir embora"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 1:
            message="A sala está repleta de esqueletos e recentes cadáveres que estão no processo de decomposição,"\
            "com tanta morte e desespero você sente o peso das almas daqueles que tiveram um fim trágico"
            
            decision1="Lutar"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_demon_Cha = [Skill("Enganação", SkillType.MANASTEALD6, 0, 0, 'str'), Skill("Controle Mental", SkillType.DIRECTD6, 6, 8, 'str'), Skill("Causar Terror", SkillType.MANASTEALD20, 4, 14, 'str')]
            skills_Skeleton_Dex = [Skill("Disparo Rápido", SkillType.DIRECTD6, 2, 0, 'str'), Skill("Chuva de Flechas", SkillType.DIRECTD6, 2, 10, 'str'), Skill("Flecha no Joelho", SkillType.DIRECTD12, 2, 20, 'str')]
            skills_Skeleton_Int = [Skill("Lança Sombria", SkillType.DIRECTD6, 1, 0, 'str'), Skill("Mísseis Mágico", SkillType.AREAD6, 3, 6, 'str'), Skill("Reconstrução", SkillType.HEALD6, 3, 10, 'str')]
                
            enemy1 = Character("Esqueleto Arqueiro",'assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png','assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png','assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png',24,30,1,0,0,0,0,0,skills_Skeleton_Dex,10,False,common_inventory)
            enemy2 = Character("Esqueleto Mago",'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Dead).png', 20,60,0,0,0,0,0,0, skills_Skeleton_Int, 10, False, common_inventory)
            enemy3 = Character("Demônio Menor ",'assets/portraits/Enemies/Demon/DemonCHA(Alive).png','assets/portraits/Enemies/Demon/DemonCHA(Alive).png', 'assets/portraits/Enemies/Demon/DemonCHA(Dead).png', 45,30,2,0,0,0,0,0, skills_demon_Cha, 10, False)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()


        if decision == 2:
            message="A sala está repleta de esqueletos e recentes cadáveres que estão no processo de decomposição,"\
            "com tanta morte e desespero você sente o peso das almas daqueles que tiveram um fim trágico"
        
            decision1="Lutar"
            decision2=None
            
            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_demon_Fai = [Skill("Machucar", SkillType.DIRECTD6, 5, 0, 'str'), Skill("Sede por Sangue", SkillType.DIRECTD12, 4, 10, 'str'), Skill("Fogo do Inferno", SkillType.AREAD12, 4, 20, 'str')]
            skills_demon_Cha = [Skill("Enganação", SkillType.MANASTEALD6, 0, 0, 'str'), Skill("Controle Mental", SkillType.DIRECTD6, 6, 8, 'str'), Skill("Causar Terror", SkillType.MANASTEALD20, 4, 14, 'str')]
            common_inventory = Inventory(0)

            enemy1 = Character("Demônio Menor ",'assets/portraits/Enemies/Demon/DemonCHA(Alive).png','assets/portraits/Enemies/Demon/DemonCHA(Alive).png', 'assets/portraits/Enemies/Demon/DemonCHA(Dead).png', 45,30,2,0,0,0,0,0, skills_demon_Cha, 10, False)
            enemy2 = Character("Demônio Maior",'assets/portraits/Enemies/Demons/DemonFAI(Alive).png','assets/portraits/Enemies/Demons/DemonFAI(Alive).png', 'assets/portraits/Enemies/Demons/DemonFAI(Dead).png', 55,60,5,0,0,0,0,0, skills_demon_Fai, 10, False, common_inventory)
            enemy3 = Character("Demônio Menor ",'assets/portraits/Enemies/Demon/DemonCHA(Alive).png','assets/portraits/Enemies/Demon/DemonCHA(Alive).png', 'assets/portraits/Enemies/Demon/DemonCHA(Dead).png', 45,30,2,0,0,0,0,0, skills_demon_Cha, 10, False)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [12],
            disable_zone_buttons = [11]
        )
 
    # 13 - Máquina de reencarnação abandonada
    def zone13(self) -> EventResponse:
        message="Você avista um tambor gigante, ele está cheio de sangue, mas aparenta ter sido abandonado a muito tempo."\
        "Há alguns pilares em volta do local aparentando ser usados para realizar o funcionamento a maquina."

        decision1="Interagir"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )    

        message="Você nota que um brilho ainda reluz de um dos pilares,"\
                "mas decide se seria melhor destrui-la ou ligar a maquina"

        decision1="Enconstar no pilar"
        decision2="Destrui-la"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:
            message="Uma luz se emite de um pilar para outro, fazendo com que a máquina seja iniciada."\
                "Um pouco sangue é derramado no chão e mãos começam a surgir e após alguns borbulhos, demônios começam a sair do tambor."\
                "Nada lhe resta a não ser enfrenta-los"

            decision1="Lutar"
            decision2=None
            
            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_demon_Fai = [Skill("Machucar", SkillType.DIRECTD6, 5, 0, 'str'), Skill("Sede por Sangue", SkillType.DIRECTD12, 4, 10, 'str'), Skill("Fogo do Inferno", SkillType.AREAD12, 4, 20, 'str')]
            skills_demon_Cha = [Skill("Enganação", SkillType.MANASTEALD6, 0, 0, 'str'), Skill("Controle Mental", SkillType.DIRECTD6, 6, 8, 'str'), Skill("Causar Terror", SkillType.MANASTEALD20, 4, 14, 'str')]
            common_inventory = Inventory(0)

            enemy1 = Character("Demônio Menor ",'assets/portraits/Enemies/Demon/DemonCHA(Alive).png','assets/portraits/Enemies/Demon/DemonCHA(Alive).png', 'assets/portraits/Enemies/Demon/DemonCHA(Dead).png', 45,30,2,0,0,0,0,0, skills_demon_Cha, 10, False)
            enemy2 = Character("Demônio Maior",'assets/portraits/Enemies/Demons/DemonFAI(Alive).png','assets/portraits/Enemies/Demons/DemonFAI(Alive).png', 'assets/portraits/Enemies/Demons/DemonFAI(Dead).png', 55,60,5,0,0,0,0,0, skills_demon_Fai, 10, False, common_inventory)
            enemy3 = Character("Demônio Menor ",'assets/portraits/Enemies/Demon/DemonCHA(Alive).png','assets/portraits/Enemies/Demon/DemonCHA(Alive).png', 'assets/portraits/Enemies/Demon/DemonCHA(Dead).png', 45,30,2,0,0,0,0,0, skills_demon_Cha, 10, False)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()


            return EventResponse(
                activity_zone_buttons = [13],
                disable_zone_buttons = [12]
            )    

        message="Com determinação, você empurra o pilar, vendo-o cair e se despedaçar no chão,"\
            " seus fragmentos mágicos se dispersando pelo ambiente. Observando o resultado,"\
            " você compreende que uma máquina tão poderosa não deve cair nas mãos erradas."

        decision1="Sair"
        decision2=None

        return EventResponse(
                activity_zone_buttons = [13],
                disable_zone_buttons = [12]
            )

    # 14 - Livros Amaldiçoados
    def zone14(self) -> EventResponse:
        message="Na biblioteca deste lugar, um véu de mistérios oculta uma miríade de segredos,"\
            " cada um oferecendo possibilidades infinitas para aqueles que os desvendam."\
            " Sem aviso, um livro é lançado aos seus pés, suas páginas folheando-se rapidamente como se guiadas por"\
            " uma força invisível, revelando fragmentos de conhecimento anteriormente ocultos."\
            " A tentação de explorar esses segredos é irresistível, ainda que a origem desse estranho fenômeno permaneça inexplicada."
        
        
        decision1="Fechar o livro"
        decision2="Ler o livro"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            message="Ao pegar o livro e folhear até a página aberta, você se depara com um texto que descreve um antigo ritual,"\
                " oferecendo a promessa da bênção do conhecimento em troca de algo valioso. Enquanto seus olhos percorrem as palavras,"\
                " você sente uma estranha sensação de impulso, e involuntariamente, as palavras do ritual escapam de seus lábios."\
                " Você percebe a presença de uma energia maligna, que parece envolver seu corpo, te enfraquecendo mas ao mesmo tempo trazendo conhecimento."

            self.equipment.inteligence = self.equipment.inteligence + 1

            for allie in self.allies:
                allie.hp = allie.hp - 10

            decision1="Sair"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)
            return EventResponse(
                activity_zone_buttons = [15],
                disable_zone_buttons = [13]
            )    
        
        message="Ao fechar o livro, uma sensação de peso se abate sobre seu corpo, mas estranhamente, "\
            "essa pressão traz consigo uma sensação reconfortante. Por um breve instante, uma onda de revitalização perpassa seu ser."\
            "Observando a capa do livro, você nota o título inscrito em letras douradas: “Escolhas e Maldições”. "\
            "Seja qual for o conteúdo dessas páginas, você compreende que ele está destinado a ser esquecido dentro dos confins sombrios desta caverna."

        for allie in self.allies:
            allie.mp = allie.mp + 25

        decision1="Sair"
        decision2=None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
                activity_zone_buttons = [15],
                disable_zone_buttons = [13]
            )

    #15 - Bote encostado
    def zone15(self) -> EventResponse:
        message = "Um bote está encostado próximo a água e seguindo por esse caminho levaria uma longa e perigosa "\
            "viagem contornando as rochas e rochedos, mas uma boa camuflagem para ninguém lhe avistar ou seguir."
        
        decision1 = "Seguir caminho" 
        decision2 = None

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        return EventResponse(
                activity_zone_buttons = [15],
                disable_zone_buttons = [14]
            )


    #16 - Voslok
    def zone16(self) -> EventResponse:

        try_take_Fhajar = False
        why_Voslok_still_here = False
        offer_to_help_Lokmar = False
        get_Fhajar = False
        face_Voslok = False
        agree_to_help = False

        message="Você avista um homem próximo de um corpo mumificado, ele aparenta estar análisando com cuidado. "\
            "Seus olhos se fixam em você, revelando um rosto marcado por uma cicatriz profunda."\
            " Ele o encara por um momento, aguardando que você quebre o silêncio com alguma palavra."
        
        decision1="Não dizer nada"
        decision2="Quem é você?"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        # 1
        if decision == 1:
            message= "Após alguns segundos de espera, ele se vira para um livro. “Me chamo Voslok e, quem quer que você seja, chegou tarde."\
                " Talvez você já tenha lidado com o restante dos Ratakaz”. Ele folheia algumas páginas. "\
                "“É uma pena o que aconteceu com eles”."
            
            decision1="Por que o Ratakaz protege esse lugar?"
            decision2="Estou aqui para coletar Fhajar"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            #1 
            if decision == 1:    
                message= "“Este local é a maldição deles, e sua civilização jurou protegê-lo para evitar que alguém causasse a destruição no mundo”,"\
                    " ele diz, fixando o olhar nos seus olhos. “Talvez você esteja aqui para isso”."
                
                decision1="“Estou aqui para coletar Fhajar”"
                decision2="“O que está fazendo aqui?”"

                decision = self.event_handler.run(self.allies, message, decision1, decision2)
                
                if decision == 1:
                    try_take_Fhajar = True         
                else:
                    why_Voslok_still_here = True
            
            else:
                try_take_Fhajar = True         

        #2
        else:
            message= "“Me chamo Voslok, mão direita de Lokmar e suspeito que você seja um mercenário”, ele declara, "\
                "encarando você com um sorriso sutil. “Acredito que acertei. Se estiver em busca de algo, chegou tarde."\
                " Este lugar foi destruído e não há mais nada aqui para encontrar.”"
            
            decision1="“Estou aqui para coletar Fhajar”"
            decision2="“O que está fazendo aqui?”"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:
                try_take_Fhajar = True         
            else:
                why_Voslok_still_here = True
        
            
        if why_Voslok_still_here == True:
            message= "“Estou aqui pelo mesmo motivo que você”, ele diz, lançando um breve olhar para o corpo mumificado"\
                " de Fhajar. “Meu objetivo é retirar Fhajar deste local e eliminar qualquer um que tente impedir”."
                          
            decision1="“Vou retira-lo daqui”"
            decision2="“Estou disposto a ajudar Lokmar”"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:
                get_Fhajar = True         
            else:
                offer_to_help_Lokmar = True 

        if try_take_Fhajar == True:    
            message= "“E você sabe o que é Fhajar?” Ele percebe sua falta de resposta e ri suavemente. "\
                "“Esse corpo diante de mim é o Fhajar, um antigo deus abandonado por seu próprio povo em favor dos novos deuses. "\
                "Fhajar jurou vingança para destruí-los”."
                
            decision1="“Vou retira-lo daqui”"
            decision2=None
            decision = self.event_handler.run(self.allies, message, decision1, decision2)
            get_Fhajar = True         
            
        if offer_to_help_Lokmar == True:
            message= "Ele fica pensativo por um instante. “Se você está aqui, eu sei quem te contratou e estou disposto a negociar”, ele afirma,"\
                "retirando uma pedra circular do bolso e jogando-a em sua direção. “Essa pedra circular abrirá um portal. Use-a quando estiver conversando"\
                "com Karadur e dará vantagem para Lokmar atacar. Você poderia usar o corpo de Fhajar como vantagem para acessar seu castelo, mas se desejar quebrar o acordo, sofrerá as consequências”."
                
            decision1="“Enfrentar Voslok”"
            decision2="“Concordar em ajudar”"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:
                face_Voslok = True
            else:
                agree_to_help = True

        if get_Fhajar == True:
            message= "Ele ri brevemente. “Se você está aqui, eu sei quem te contratou e estou disposto a negociar.”"\
                "Ele retira uma pedra circular do bolso e a lança em sua direção. “Esta pedra circular abrirá um portal. "\
                "Use-a quando estiver conversando com Karadur e dará uma vantagem para Lokmar atacar. Mesmo que deseje me matar, você pode decidir o que fazer no futuro, mas lembre-se, não será fácil me derrotar.”"
            
            decision1="“Enfrentar Voslok”"
            decision2="“Concordar em ajudar”"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:
                face_Voslok = True
            else:
                agree_to_help = True
        
        if agree_to_help == True:
            message = "“Estarei te entregando Fhajar, mas lembre-se, se me trair, você terá consequências graves”,"\
                 " ele adverte, afastando-se do corpo e deixando você pegá-lo."    
           
            decision1="Sair do local"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if face_Voslok == True:
            message = "“Você fez uma péssima decisão”, Voslok diz enquanto se prepara para te atacar."
            
            decision1="Lutar"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_Voslok_Cha = [Skill("Ataque Sombrio", SkillType.DIRECTD6, 2, 0, 'str'), Skill("Voltar as Sombras Menor", SkillType.MANAREGEND20, 1, 5, 'str'), Skill("Cura Sombria Menor", SkillType.HEALD20, 0, 5, 'str')]
            skills_Voslok = [Skill("Orbe Negro", SkillType.DIRECTD6, 8, 0, 'str'), Skill("Ataque Sombrio Maior", SkillType.DIRECTD20, 7, 10, 'str'), Skill("Fogo Negro", SkillType.AREAD12, 6, 15, 'str')]
            skills_Voslok_Str = [Skill("Ataque Sombrio Menor", SkillType.DIRECTD6, 0, 0, 'str'), Skill("Ataque Sombrio", SkillType.DIRECTD6, 2, 8, 'str'), Skill("Ataque Sombrio Maior", SkillType.DIRECTD20, 7, 15, 'str')]
            
            common_inventory = Inventory(0)

            enemy1 = Character("Voslok Clone Frágil",'assets/portraits/Enemies/Bosses/VoslokCHA(Alive).png','assets/portraits/Enemies/Bosses/VoslokCHA(Alive).png', 'assets/portraits/Enemies/Bosses/VoslokCHA(Dead).png', 25,40,3,0,0,0,0,0, skills_Voslok_Cha, 10, False,common_inventory)
            enemy2 = Character("Voslok",'assets/portraits/Enemies/Bosses/Voslok(Alive).png','assets/portraits/Enemies/Bosses/Voslok(Alive).png', 'assets/portraits/Enemies/Bosses/Voslok(Dead).png', 100,40,4,0,0,0,0,0, skills_Voslok, 10, False,common_inventory)
            enemy3 = Character("Voslok Clone Forte",'assets/portraits/Enemies/Bosses/VoslokSTR(Alive).png','assets/portraits/Enemies/Bosses/VoslokSTR(Alive).png', 'assets/portraits/Enemies/Bosses/VoslokSTR(Dead).png', 50,5,7,0,0,0,0,0, skills_Voslok_Str, 10, False,common_inventory)
            
            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [],
            disable_zone_buttons = []
        )