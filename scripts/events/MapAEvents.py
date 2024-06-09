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

class MapAEvents:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, allies, equipment)

    def zone1(self) -> EventResponse:
        message="Avistando um rochedo pequeno em meio a água, você identifica que além do brilho de luz emitido pelo"\
             " fogo mágico, algo reluz entre ele. Com um gancho e uma boa pontaria talvez seja possível pegar esse item."
       
        decision1="Usar o gancho"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        dexterity_total = self.allies[0].dexterity + self.allies[1].dexterity + self.allies[2].dexterity + roll

        if dexterity_total >= 15:
                for allie in self.allies:
                    allie.mp = allie.mp + 10
                
                message= f"Resultado({dexterity_total}) - Teste(15): "\
                        "Com sua boa pontaria você arremessa o gancho e com cuidado começa a puxar,"\
                        " fazendo com que o item caia na água, mas esteja bem preso ao seu gancho. Ao se aproximar,"\
                        "você identifica que se trata de um cristal de mana, sendo útil para aventureiros como você."

                decision1="Sair"
                decision2=None
                
                self.event_handler.run(self.allies, message, decision1, decision2)
    
        else:
            message= f"Resultado({dexterity_total}) - Teste(15): "\
                "Você arremessa o gancho e se certifica que está preso, mas ao puxar, o item acaba se soltando"\
                "do gancho e indo para as profundezas da água."

            decision1="Sair"
            decision2=None
                
            self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [],
            disable_zone_buttons = [0]
            )
    
    #2 - Barcos recentes
    def zone2(self) -> EventResponse:
        message="Você encontra alguns botes que aparentam ter chegado recentemente no local, há algumas coisas dentro dele"

        decision1="Vasculhar o bote"
        decision2="Não mexer no bote"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:
            for allie in self.allies:
                    allie.mp = allie.mp - 10

            message = "Decidindo vasculhar você percebe que seu tempo foi em vão e que às vezes a ganância por algo pode ser uma perca de tempo."
            
            decision1="Sair"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)

        if decision2 == 2:
            for allie in self.allies:
                    allie.mp = allie.mp + 5

            message = "Sabendo que não há nada útil ali você decide seguir seu caminho e"\
                " sabe que a ganância por algo pode ser uma perca de tempo."

            decision1="Sair"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)
             
        return EventResponse(
            activity_zone_buttons = [2,3,4],
            disable_zone_buttons = [1]
            )
    
    #3 - Corredor Estreito
    def zone3(self) -> EventResponse:
        message="Seguindo a beira das rochas, você se encontra com uma passagem estreita e em seu caminho está repleto"\
            "de restos mortais de animais que morreram a muito tempo, e você sabe que já não se encontra mais nenhuma"\
            "vida nessas redondezas."

        decision1="Prosseguir"
        decision2="Voltar"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:
            message = "Decidido a seguir, a cada passo você ouve o estalar de ossos se"\
                " quebrando e emitindo um som irritante, mas que já tem o costume de ouvir."\
                " Você conclui o caminho e percebe que quem ou qual ser usou esse local de refúgio já deve o ter abandonado a muito tempo."
            
            decision1="Prosseguir"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)
            
            return EventResponse(
                activity_zone_buttons = [9,10],
                disable_zone_buttons = [2]
                )
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
                )
        
    #4 - Aranhas nas ruínas
    def zone4(self) -> EventResponse:
        message="Este lugar aparentava conter diversas construções, que se foram ao longo do tempo. Você não sabe o"\
            " que estava aqui e provavelmente nunca descobrirá, mesmo as aranhas já tenham desistido desse lugar,"\
            " deixando suas teias e os restos de seus alimentos."

        decision1="Sair"
        decision2= None

        self.event_handler.run(self.allies, message, decision1, decision2)
            
        return EventResponse(
            activity_zone_buttons = [],
            disable_zone_buttons = [3]
            )

     #5 - Santuário
    def zone5(self) -> EventResponse:
        message="Você encontra um antigo santuário com dois sarcófagos. Em um pedestal está a escultura de um"\
            "  deus e você tenta reconhece-lo."\
            
        decision1="Interagir"
        decision2="Voltar"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        faith_total = self.allies[0].faith + self.allies[1].faith + self.allies[2].faith + roll

        if faith_total >= 15:
                message= f"Resultado({faith_total}) - Teste(15): "\
                        "Esse é o deus das dimensões, cultuado por uma civilização muito antiga chamada Ratakaz. "\
                        "Eles acreditavam que todos os mortos enterrados desapareciam de seus túmulos e eram levados para "\
                        " um novo mundo. Sabendo disso, você recorda que é um sacrilégio abrir esses sarcófagos."

                decision1="Sair"
                decision2=None
                   
                self.event_handler.run(self.allies, message, decision1, decision2)
    
        else:
            for allie in self.allies:
                    allie.hp = allie.hp - 10
                    if allie.hp <= 0:
                        allie.hp = 1
                    
            message= f"Resultado({faith_total}) - Teste(15): "\
                "Você não conhece esse deus, então decide abrir os sarcófagos para encontrar algo útil. No momento "\
                " que abre uma fresta o sarcófago é destruido, arremessando seus pedaços em todas direções. Você "\
                " descobre da pior forma que aquele deus era fortemente ligado a esse sarcófago."


            decision1="Sair"
            decision2=None
                
            self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [5],
            disable_zone_buttons = [4]
            )
    
    #6 - Entulhos
    def zone6(self) -> EventResponse:
        message="Com um cheiro horrível e diversos itens quebrados, esse local está tão degradado que nunca "\
            " mais poderá ser utilizado. Mas alguns itens como roupas e armaduras te intrigam, pois são maiores"\
            " que as de um humano normal."
            
        decision1="Interagir"
        decision2="Voltar"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:
            message = "Mesmo com o cheiro ruim, você se interessa em saber o que está armazenado ali. Avistando restos de "\
                " corpos, de alimentos e itens com diversos símbolos, como o de um homem com cabeça de rato, permanecem em "\
                " meio aos destroços. Sem saber o que isso significa, você desiste da procura pois o cheiro se torna insuportável."
                
            decision1="Prosseguir"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)
            
            return EventResponse(
                activity_zone_buttons = [6,7,8,10,11],
                disable_zone_buttons = [5]
                )
        else:
            return EventResponse(
                activity_zone_buttons = [6,7,8,10,11],
                disable_zone_buttons = [5]
                )

    #7 - Escavação antiga
    def zone7(self) -> EventResponse:
        message="Aqui estão alguns equipamentos de escavação que foram consumidos pela poeira, detritos e ferrugem "\
            " formada com o decorrer do tempo. Dentre os equipamentos está uma engenhosa máquina, que você nunca viu. "
        
        decision1="Interagir"
        decision2="Voltar"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 1:
            message = "Você percebe que ela era utilizada para coletar e moer geodos, sendo depositados em um compartimento"\
                " selado. Utilizando um pouco de força, você abre o compartimento e vê diversas pedras raras, são tantas que "\
                " seria impossível levar todas."
                            
            # Obs.: Aqui pode ser acrescentado um Reasultado =  +1 de STR
            
            decision1="Prosseguir"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)
            
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = [6]
                )
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
                )

    #8 - Acampamento recente
    def zone8(self) -> EventResponse:
        message="Esse acampamento foi utilizado recentemente por um grupo pequeno. No entanto, algo muito estranho ocorreu para"\
            " que deixassem a fogueira acesa e os utensílios de pesquisa abandonados no local, onde ouvia-se apenas o barulho"\
            " do estalar da lenha ao fogo."
    
        decision1="Interagir"
        decision2="Voltar"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 1:
            message = "Você decide que é bom esticar as pernas e respirar fundo, aproveitando o tempo e os recursos que foram "\
                " deixados aqui. Por um longo instante tudo está quieto, até a chegada de um homem rato que o encara com agressividade."    
        
            decision1="lutar"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)
            
            skills_Ratakaz_Dex = [Skill("Corte Leve", SkillType.DIRECTD6, 1, 0, 'str'), Skill("Corte Profundo", SkillType.DIRECTD6, 2, 5, 'str'), Skill("Punhalada", SkillType.DIRECTD6, 5, 15, 'str')]
            skills_Ratakaz_Str = [Skill("Corte Leve", SkillType.DIRECTD6, 2, 0, 'str'), Skill("Corte Profundo", SkillType.DIRECTD6, 2, 5, 'str'), Skill("Mordida", SkillType.DIRECTD12, 1, 15, 'str')]
            
            common_inventory = Inventory(0)
            
            enemy1 = Character("Ratakaz Esguio",'assets/portraits/Enemies/Ratman/RatakazDex(Alive).png','assets/portraits/Enemies/Ratman/RatakazDex(Alive).png', 'assets/portraits/Enemies/Ratman/RatakazDex(Dead).png', 15,25,2,0,0,0,0,0, skills_Ratakaz_Dex, 10, False, common_inventory)
            enemy2 = Character("Ratakaz Esguio",'assets/portraits/Enemies/Ratman/RatakazDex(Alive).png','assets/portraits/Enemies/Ratman/RatakazDex(Alive).png', 'assets/portraits/Enemies/Ratman/RatakazDex(Dead).png', 15,25,2,10,10,10,10,1, skills_Ratakaz_Dex, 10, False, common_inventory)
            enemy3 = Character("Ratakaz Forte",'assets/portraits/Enemies/Ratman/RatakazSTR(Alive).png','assets/portraits/Enemies/Ratman/RatakazSTR(Alive).png', 'assets/portraits/Enemies/Ratman/RatakazSTR(Dead).png', 20,15,3,10,10,10,10,1, skills_Ratakaz_Str, 10, False, common_inventory)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()
            
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = [7]
                )
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
                )

    
    #9 - Globo de cristal
    def zone9(self) -> EventResponse:
        message= "O caminho está manchado por sangue, mesmo sem nenhum corpo em volta. "\
            "No centro da sala está um globo de vidro e ao se aproximar você nota que dentro dele possui algo, "\
            "mas não consegue identificar o que seja."
            
        decision1="Quebrar o vidro"
        decision2="Deixar o cristal"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:
            message= "Com um poderoso golpe, o vidro se racha. Um líquido gosmento começa a escorrer e com o estilhaçar do vidro, "\
                "dois embriões com aparência humana deformada. Eles estavam armazenados para preservar suas vidas, "\
                "você nota que não há mais salvação para aquelas vidas."

            decision1="Sair"
            decision2=None
        
            self.event_handler.run(self.allies, message, decision1, decision2)
        else:
            message="Há coisas das quais é melhor se manter intacta, com isso em mente você decide deixar a sala e segue seu caminho."
            
            decision1="Sair"
            decision2=None

            self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [],
            disable_zone_buttons = [8]
            )

    #10 - Presença na água
    def zone10(self) -> EventResponse:
        message= "Após um longo caminho com a água em seu joelho, você encontra um poço com diversas estátuas exibindo a feição neutra. "\
        "Algo aparenta estar no fundo do poço lhe observando e uma sensação te chama para entrar na água."
        
        decision1="Entrar na água"
        decision2="Voltar"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 1:

            roll = DiceRow.dice6()
            charisma_total = self.allies[0].charisma + self.allies[1].charisma + self.allies[2].charisma + roll

            if charisma_total >= 10:
                for allie in self.allies:
                    allie.hp = allie.hp + 20
                    allie.mp = allie.mp + 15
                
                message= f"Resultado({charisma_total}) - Teste(10): "\
                "Após um salto repentino, você afunda e a única luz acima de você some, deixando apenas a escuridão. " \
                "Sem se desesperar você nota que a sensação de olhar surge, mas dessa vez trazendo paz para sua mente. "\
                "A luz ressurge e ao sair você nota que todas as estátuas estão sorrindo"
            
                decision1="Sair"
                decision2=None
        
                self.event_handler.run(self.allies, message, decision1, decision2)
            
            else:
                for allie in self.allies:
                    allie.hp = allie.hp - 20
                    allie.mp = allie.mp - 15
                    if allie.hp <= 0:
                        allie.hp = 1
                    if allie.mp <= 0:
                        allie.mp = 1 
   
                message= f"Resultado({charisma_total}) - Teste(10): "\
                "Após um salto repentino você afunda e a única luz acima de você some deixando apenas a escuridão. "\
                "Com desespero, você teme por sua vida e a sensação de presença, algo o expulsa da água. "\
                "Após ser arremessado você percebe a feição das estátuas, estão tristes."

                decision1="Sair"
                decision2=None
        
                self.event_handler.run(self.allies, message, decision1, decision2)
            
        return EventResponse(
            activity_zone_buttons = [],
            disable_zone_buttons = [9]
            )

    #11 - Ponte perigosa
    def zone11(self) -> EventResponse:
        message="Com passos cuidadosos você tenta atravessar a ponte, que está bem deteriorada, devido ao abandono. A cada passo, o ranger "\
            " da madeira ecoa pelas paredes, se misturando com o barulho de água, que corre abaixo da ponte. Você toma precauções para "\
            " evitar um acidente."
       
        decision1="Interagir"
        decision2="Voltar"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )
        
        roll = DiceRow.dice6()
        dexterity_total = self.allies[0].dexterity + self.allies[1].dexterity + self.allies[2].dexterity + roll

        if dexterity_total >= 18:
                                
                message= f"Resultado({dexterity_total}) - Teste(18): "\
                        "Com passos leves e muito cuidado e percebendo que cair na água poderia trazer graves "\
                        " consequências ou até a morte, você atravessa a ponte sem que nenhum evento trágico"\
                        " aconteça."

                decision1="Sair"
                decision2=None
                
                self.event_handler.run(self.allies, message, decision1, decision2)
    
        else:
            for allie in self.allies:
                    allie.hp = allie.hp - 10
                    if allie.hp <= 0:
                        allie.hp = 1
            
            message= f"Resultado({dexterity_total}) - Teste(18): "\
                "A madeira quebra fazendo-o cair. Com rapidez você se apoia, com força, na corda garantindo sua"\
                " sobrevivência. Entretanto o dano nas mãos gerou um leve sangramento. Mas, graças a sua agilidade, você"\
                " volta a ficar firme e segue com seus passos cuidadosos."

            decision1="Sair"
            decision2=None
                
            self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [6,7,8,10,11],
            disable_zone_buttons = [10]
            )

    # Entrada da caverna
    def zone12(self) -> EventResponse:
        message= "Percorrendo um caminho estreito e improvisado, você é surpreencido por corpos que morreram recentemente. "\
        "Alguns foram emboscados, perceptível por suas espadas estarem na bainha. No final do caminho há um grupo de homem rato, "\
        "dentre eles há um maior que ao lhe avistar, começa a caminhar em sua direção."
        
        decision1="Interagir"
        decision2=None
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        #-------------------------------------------------------------------
        message = "Vocês profanaram este local. Meu povo se dedicou a mante-lo escondido de vocês…”"\
        " o homem rato possue uma ferida visivel no abdomem."\
        "“Alguns passaram, mas não vou deixar todos entrarem.” Os que restaram começam a lhe cercar"
        
        decision1="Não estou com eles"
        decision2="Quem são vocês?"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        #=====================================================================================#
        if decision == 1:
            message = "Te olhando de cima a baixo, ele te examina. “Você não se parece com eles, mas pode ter o mesmo motivo.” "\
                "Ele se aproxima mostrando seus dentes afiados. “Esse local é sagrado e é nosso dever protegê-lo”"
        else:
              message = "Te olhando de cima a baixo, ele te examina - “Somos igual a vocês, mas para vocês não somos iguais”."\
                " Ele se aproxima mostrando seus dentes afiados - “Esse local é sagrado e é nosso dever protegê-lo”"
        
        decision1="O que vocês querem?"
        decision2="Por que mataram eles"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        #=====================================================================================#
        if decision == 1:
            message = "Nosso único desejo é que vocês vão embora e nos deixem em paz, já sofremos por causa de vocês”. "\
            "Com dor em sua fala e tristeza em seu rosto ele se vira para a descida. “Nosso povo se chama Ratakaz, "\
            "estamos protegendo esse local a anos”."
        else:
              message = "“Eles profanaram o local, impedimos alguns mas não temos mais forças para os outros”. "\
            "Com dor em sua fala e tristeza em seu rosto ele se vira para a descida. "\
            "“Nosso povo se chama Ratakaz, estamos protegendo esse local a anos”."

        decision1="O que aconteceu com seu povo?"
        decision2="Preciso descer"
        
        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        #=====================================================================================#
        if decision == 1:
            message ="“Meu povo… meu povo”. Com um olhar pensante ele estanca o sangue"\
            "“Meu povo era grande e vivia em um lugar lindo e longe daqui, mas graças a maldição dele, fomos diminuindo com o tempo."\
            "Decidimos nos abrigar aqui e fortificar o local até o fim de nossas vidas”."       
        else:
              message = "“Não deixarei e mesmo que passe não serei o único a impedi-lo”."\
                " Com a mão em sua lâmina ele te encara e seus aliados se preparam para luta. "\
                "“Você tem a decisão de ir embora ou terminar nesse local”"

        decision1="Persuadir"
        decision2="Iniciar combate"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        roll = DiceRow.dice6()
        charisma_total = self.allies[0].charisma + self.allies[1].charisma + self.allies[2].charisma + roll

        if charisma_total >= 18 and decision == 1:
            message = f"Resultado({charisma_total}) - Teste(18): "\
                "“Realmente, você não se demonstrou ser igual aos outros” "\
                "ele da espaço  e se senta ao chão para recuperar suas energias. "\
                "“Há mais coisas lá em baixo, tome cuidado”."
                
            decision1="Seguir"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = [11]
                )
        else:       
            message = f"Resultado({charisma_total}) - Teste(18): "\
                "“Não deixarei e mesmo que passe não serei o único a impedi-lo”."\
                " Com a mão em sua lâmina ele te encara e seus aliados se preparam para luta. "\
                "“Você tem a decisão de ir embora ou terminar nesse local”"

            decision1="Lutar"
            decision2=None

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            
            skills_Ratakaz_Dex = [Skill("Corte Leve", SkillType.DIRECTD6, 1, 0, 'str'), Skill("Corte Profundo", SkillType.DIRECTD6, 2, 5, 'str'), Skill("Punhalada", SkillType.DIRECTD6, 5, 15, 'str')]
            skills_Ratakaz_Str = [Skill("Corte Leve", SkillType.DIRECTD6, 2, 0, 'str'), Skill("Corte Profundo", SkillType.DIRECTD6, 2, 5, 'str'), Skill("Mordida", SkillType.DIRECTD12, 1, 15, 'str')]
            skills_Ratakaz_King = [Skill("Corte Profundo", SkillType.DIRECTD6, 5, 0, 'str'), Skill("Mostrar as Presas", SkillType.MANASTEALD20, 0, 10, 'str'), Skill("Fúria Ratakaz", SkillType.DIRECTD20, 0, 15, 'str')]
            
            common_inventory = Inventory(0)
            
            enemy1 = Character("Ratakaz Esguio",'assets/portraits/Enemies/Ratman/RatakazDex(Alive).png','assets/portraits/Enemies/Ratman/RatakazDex(Alive).png', 'assets/portraits/Enemies/Ratman/RatakazDex(Dead).png', 15,25,2,0,0,0,0,0, skills_Ratakaz_Dex, 10, False, common_inventory)
            enemy2 = Character("Ratakaz Rei",'assets/portraits/Enemies/Bosses/RatakazKing(Alive).png','assets/portraits/Enemies/Bosses/RatakazKing(Alive).png', 'assets/portraits/Enemies/Bosses/RatakazKing(Dead).png', 50,50,4,10,10,10,10,1, skills_Ratakaz_King, 10, False, common_inventory)
            enemy3 = Character("Ratakaz Forte",'assets/portraits/Enemies/Ratman/RatakazSTR(Alive).png','assets/portraits/Enemies/Ratman/RatakazSTR(Alive).png', 'assets/portraits/Enemies/Ratman/RatakazSTR(Dead).png', 20,15,3,10,10,10,10,1, skills_Ratakaz_Str, 10, False, common_inventory)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = [11]
                )    