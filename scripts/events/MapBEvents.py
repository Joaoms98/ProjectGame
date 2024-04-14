from response.EventResponse import EventResponse
from response.BattleResponse import BattleResponse
from scripts.CharacterSelect import CharacterSelect
from objects.Skill import Skill
from utils.enums.SkillType import SkillType
from objects.Character import Character
from scripts.Arena import Arena
from scripts.EventHandler import EventHandler

class MapBEvents:
    def __init__(self, screen, screen_rect, fps, resolution, allies, equipment):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution
        self.allies = allies
        self.equipment = equipment
        self.event_handler = EventHandler(self.screen, self.screen_rect, self.fps, self.resolution, allies, equipment)

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

            faith_total = self.allies[0].faith + self.allies[1].faith + self.allies[2].faith
            self.equipment.faith = self.equipment.faith + 1

            if faith_total == 1:

                for allie in self.allies:
                    allie.hp = allie.hp - 1

                message= "Graças aos anos de estudos em teologia,"\
                        "você identifica que símbolo é dedicado ao deus"\
                        "da dor e da colheita de uma religião que a muito"\
                        "tempo foi extinta, sendo acusados de sacrificar"\
                        "humanos para crescimento de suas plantações. Com seu"\
                        "conhecimento você faz uma oferenda de sangue e cita"\
                        "uma reza para terra em troca do amuleto."
                decision1="Ave maria"
                decision2="Cruz credo"
                self.event_handler.run(self.allies, message, decision1, decision2)
            else:
                message= "Você não consegue identificar aquele símbolo mas mesmo assim decide "\
                        "pegar o amuleto. No momento em que você o toca, o corpo esquelético agarra "\
                        "sua mão e você salta para trás conseguindo se afastar e manter o amuleto em "\
                        "suas mãos, porém você nota que mais corpos se levantam mostrando que mesmo mortos "\
                        "eles estão dispostos a lutar."
                decision1="Que pena!"
                decision2="Droga!"
                decision = self.event_handler.run(self.allies, message, decision1, decision2)

                skills_test = [Skill("attackdirect", SkillType.DIRECTD6, 1, 1, 'str'), Skill("attackarea", SkillType.AREAD12, 1, 1, 'str'), Skill("attackheal", SkillType.HEALD12, 1, 1, 'str')]

                enemy1 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonDEX(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
                enemy2 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
                enemy3 = Character("Esqueleto",'assets/portraits/Enemies/Skeleton/SkeletonSTR(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonSTR(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

                arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
                battleResponse = arena.run()

                return EventResponse(
                    activity_zone_buttons = [2, 3],
                    disable_zone_buttons = [0]
                )

    def zone2(self) -> EventResponse:
            message="Próximo ao fluxo de água, há algumas velas em algo que parece ser uma oferenda "\
                    ". Você se pergunta por que e para que serve essa oferenda"
            decision1="Destruir a oferenda "
            decision2="Jogar a oferenda na água"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            if decision == 1:

                message="Você decide destruir a oferenda, porém nada acontece. Talvez seja melhor assim."
                decision1="Sair"
                decision2="Sair"

                decision = self.event_handler.run(self.allies, message, decision1, decision2)

                return EventResponse(
                    activity_zone_buttons = [2],
                    disable_zone_buttons = [1]
                )

            message="Você decide jogar a oferenda na água, após alguns instantes um afogado aparece "\
                    "mostrando toda sua fúria. Você percebe que não foi a melhor decisão."
            decision1="Droga"
            decision2="Saco"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            skills_test = [Skill("attackdirect", SkillType.DIRECTD6, 1, 1, 'str'), Skill("attackarea", SkillType.AREAD6, 1, 1, 'str'), Skill("attackheal", SkillType.HEALD12, 1, 1, 'str')]

            enemy1 = Character("Afogado",'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
            enemy2 = Character("Afogado",'assets/portraits/Enemies/Drowned/DrownedMonsterINT(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonINT(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
            enemy3 = Character("Afogado",'assets/portraits/Enemies/Drowned/DrownedMonsterDEX(Alive).png', 'assets/portraits/Enemies/Skeleton/SkeletonDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

            arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
            battleResponse = arena.run()

            return EventResponse(
                activity_zone_buttons = [2],
                disable_zone_buttons = [1]
            )

    def zone3(self) -> EventResponse:
        message="Você encontra um local com diversos cogumelos e percebe que alguém se dedicou "\
                "a cuidar desse lugar. Talvez há algo que você possa pegar, mas tem dificuldade em "\
                "identificar qual cogumelo levar."
        decision1="Vasculhar "
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        intelligence_total = self.allies[0].intelligence + self.allies[1].intelligence + self.allies[2].intelligence + self.equipment.intelligence

        if intelligence_total > 1:
            message="Ao vasculhar, você encontra alguns cogumelos da realeza, conhecidos por "\
                "fortalecer e recarregar a energia daqueles que o ingerem. "\
                "(Todos os aliados reabastece + 4 vida, 8 de mana e 10 de vigor)"
            decision1="nhãm nhãm"
            decision2="Sair"

            for allie in self.allies:
                allie.hp  = allie.hp + 4
                allie.mp = allie.mp + 8
                allie.st = allie.st + 10

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )

        elif intelligence_total ==  1:
            message="Mesmo após vasculhar diversas vezes, você não reconhece nenhum deles e decide  "\
                    "que é melhor deixá-los de lado."
            decision1="Sair"
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )
        else:
            message="Ao vasculhar, você se atrai por um cogumelo brilhante e decide ingeri-lo, mas "\
                    "percebe que não foi a coisa certa."
            decision1="Sair"
            decision2="Sair"

            for allie in self.allies:
                allie.hp  = allie.hp - 1
                allie.mp = allie.mp - 1
                allie.st = allie.st - 1

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [3, 4, 5],
                disable_zone_buttons = [2]
            )

    def zone4(self) -> EventResponse:
        message="Uma longa passagem estreita está coberta de ovos abertos de aranhas mutantes, é "\
                "possível avistar alguns exploradores que não tiverem sorte e acabaram enrolados "\
                "por teias. Você acaba notando que os cadáveres morreram recentemente e seus "\
                "equipamentos estão em um bom estado, mas sabe que não será fácil removê-los "\
                "das teias."
        decision1="Remover "
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)
        
        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        strength_total = self.allies[0].strength + self.allies[1].strength + self.allies[2].strength + self.equipment.strength

        if strength_total > 1:
            message="Você consegue usar sua força para cortar os fios grossos de teias sem dificuldade, "\
                    "deixando os cadáveres acessíveis. Ao coletar os equipamentos, você nota que na "\
                    "armadura de um explorador está o símbolo do reino de Karadur e se pergunta por "\
                    "que um soldado do rei estaria nesse local. "
            decision1="Confirmar "
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            for allie in self.allies:
                allie.defense  = allie.defense + 1

        else: 
            message="Mesmo usando sua força e técnica você não consegue romper os fios de teias, após "\
                    "desistir e olhar por alguns segundos para o cadáver você nota que em sua "\
                    "armadura está o símbolo do reino de Karadur e se pergunta por que um soldado do    "\
                    "rei estaria nesse local. "
            decision1="Prosseguir "
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [2, 4],
            disable_zone_buttons = [3]
        )

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
        decision1="Lutar "
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        skills_test = [Skill("attackdirect", SkillType.DIRECTD6, 1, 1, 'str'), Skill("attackarea", SkillType.AREAD6, 1, 1, 'str'), Skill("attackheal", SkillType.AREAD20, 1, 1, 'str')]

        enemy1 = Character("aranha",'assets/portraits/Enemies/Spider/SpiderDEX(Alive).png', 'assets/portraits/Enemies/Spider/SpiderDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
        enemy2 = Character("aranha",'assets/portraits/Enemies/Spider/SpiderINT(Alive).png', 'assets/portraits/Enemies/Spider/SpiderINT(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
        enemy3 = Character("aranha",'assets/portraits/Enemies/Spider/SpiderDEX(Alive).png', 'assets/portraits/Enemies/Spider/SpiderDEX(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

        arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
        battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [7],
            disable_zone_buttons = [4]
        )

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
        decision2="Tentar fugir"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        skills_test = [Skill("attackdirect", SkillType.DIRECTD6, 1, 1, 'str'), Skill("attackarea", SkillType.AREAD6, 1, 1, 'str'), Skill("attackheal", SkillType.AREAD20, 1, 1, 'str')]
        
        enemy1 = Character("slime",'assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
        enemy2 = Character("slime",'assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)
        enemy3 = Character("slime",'assets/portraits/Enemies/Slime/Slime(Alive).png', 'assets/portraits/Enemies/Slime/Slime(Dead).png', 10,10,1,10,10,10,10,1, skills_test, 10, False)

        arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, self.allies, (enemy1, enemy2, enemy3), self.equipment)
        battleResponse = arena.run()

        return EventResponse(
            activity_zone_buttons = [11],
            disable_zone_buttons = [6]
        )
    
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

        strength_total = self.allies[0].strength + self.allies[1].strength + self.allies[2].strength + self.equipment.strength

        if strength_total > 1:

            message="Com uma boa pancada na estrutura você consegue derrubar a pilha de móveis "\
                    "improvisados para impedir o caminho, percebendo que qualquer monstro desse "\
                    "local poderia fazer o mesmo."
            decision1="Prosseguir"
            decision2="Avançar"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

            return EventResponse(
                activity_zone_buttons = [14],
                disable_zone_buttons = [7]
            )

        message="Mesmo com sua força os móveis e tábuas improvisadas ainda permanecem em pé, "\
                "você acaba se cansando e decide que é melhor encontrar outro caminho."
        decision1="Prosseguir"
        decision2="Avançar"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

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

        intelligence_total = self.allies[0].intelligence + self.allies[1].intelligence + self.allies[2].intelligence + self.equipment.intelligence

        if intelligence_total > 1:
            message="As inscrições citam um conto antigo que pertence às terras do Céu Vermelho, "\
                    "citando o amor de um casal que se entregaram ao deus do fogo para "\
                    "permanecerem unidos e combater o mal no pós vida. Você se sente inspirado, mas "\
                    "logo percebe que os exploradores são um casal e infelizmente perderam a vida "\
                    "nesse local."
            decision1="Prosseguir"
            decision2="Sair"
            decision = self.event_handler.run(self.allies, message, decision1, decision2)
        else:
            message="Você não consegue identificar o que as inscrições passam, mas sabe que antes de "\
                    "morrerem aqueles exploradores tentaram transmitir algo para o mundo."
            decision1="Prosseguir"
            decision2="Sair"
            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [9],
            disable_zone_buttons = [8]
        )
    
    def zone10(self) -> EventResponse:
        message="Você avista uma cela e se pergunta por que algo como isso está dentro dessa "\
                "caverna, no fundo dela há um homem surrado e em pânico ao te ver, ele diz “Por "\
                "favor eu já sofri muito, acabe comigo de uma vez”. Você se aproxima da cela e diz "\
                "“você tem minha palavra que vou te tirar com segurança daqui”, o homem se "\
                "aproxima de você."
        decision1="Aguardar"
        decision2="Sair"

        decision = self.event_handler.run(self.allies, message, decision1, decision2)

        if decision == 2:
            return EventResponse(
                activity_zone_buttons = [],
                disable_zone_buttons = []
            )

        charisma_total = self.allies[0].charisma + self.allies[1].charisma + self.allies[2].charisma + self.equipment.charisma

        if charisma_total > 1:
            message="“Você não está com Voslok?” com uma expressão de esperança ele se aproxima da "\
                    "grade, “Você deve acabar com ele, sua paranoia com aquele cadáver levou todos "\
                    "nós à morte e ele sequer se preocupou com isso. você deve fugir”, homem com "\
                    "tamanha destreza alcança a faca em sua cintura e rapidamente corta a garganta. "\
                    "Você nada pode fazer, apenas assistir aquele pobre homem morrer."
            decision1="Assistir"
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)
        else: 
            message="“Você… Você não devia estar aqui, todos irão morrer, aquele… aquele maldito "\
                    "cadaver”, o homem com tamanha destreza alcança a faca em sua cintura e "\
                    "rapidamente corta a garganta. Você nada pode fazer, apenas assistir aquele pobre "\
                    "homem morrer."
            decision1="Assistir"
            decision2="Sair"

            decision = self.event_handler.run(self.allies, message, decision1, decision2)

        return EventResponse(
            activity_zone_buttons = [10],
            disable_zone_buttons = [9]
        )