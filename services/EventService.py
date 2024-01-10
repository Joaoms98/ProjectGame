from response.EventResponse import EventResponse
from scripts.Arena import Arena
from objects.character import Character

class EventService:
    def __init__(self, screen, screen_rect, fps, resolution):
        self.screen = screen
        self.screen_rect = screen_rect
        self.fps = fps
        self.resolution = resolution

    def TakeEvent(self, eventId: str, decision: int = None, allies: list = None) -> EventResponse: 
        if eventId == "A1_1":
            return self.EventA1_1()
        if eventId == "A1_1_2":
            return self.EventA1_1_2(decision, allies)
        if eventId == "A2_1":
            return self.EventA2_1()
        if eventId == "A2_1_2":
            return self.EventA2_1_2(decision, allies)

    ########### Map A #############
    def EventA1_1(self) -> EventResponse:
            return EventResponse(
                message="Ao chegar no local, voce se depera com uma estranha formacao aparentando"\
                    "ser um lago e em seu cento ha um pilar de pedra reluzindo um possivel"\
                    "artefato. Com uma boa pontaria e possivel jogar um gancho para pegar o item",
                decision1="Interagir",
                decision2="Sair",
                back = False,
                completed = False
            )

    def EventA1_1_2(self, decision: int, allies: list) -> EventResponse: 
        if decision == 1:
            dexterity_count = allies[0].dexterity + allies[1].dexterity + allies[0].dexterity
            if dexterity_count > 20:
                allies[0].hp = allies[0].hp+1
                allies[1].hp = allies[1].hp+1
                allies[2].hp = allies[2].hp+1

                return EventResponse(
                    allies= allies,
                    message="Sua equipe consegue jogar o gancho e pega o artefato, dando +1 de vida para todos os aliados",
                    decision1= "Que Bom!",
                    decision2="Grande Merda!",
                    back = False,
                    completed = True    
                )
            else:
                allies[0].hp = allies[0].hp - 50
                return EventResponse(
                    allies= allies,
                    message=f"Sua equipe nao conseuge jogar o gancho, {allies[0].name} sofreu uma queda reduzindo sua vida",
                    decision1="PQP viu",
                    decision2="Ah vai se fuder",
                    back= False,
                    completed = True
                )
        if decision == 2:
            return EventResponse(
                    back = True,
                    completed = False   
                )
    
    def EventA2_1(self) -> EventResponse:
        return EventResponse(
            message="Ao chegar no local, voce se depera com uma estranha formacao aparentando"\
                "um ser esquisito lambe seu pé e pede um biscoito",
            decision1="dar um biscoito",
            decision2="sair na porrada",
            back = False,
            completed = False
        )
    
    def EventA2_1_2(self, decision: int, allies: list) -> EventResponse: 
        if decision == 1:
            return EventResponse(
                message="O ser agradece e te manda tomar no cu",
                back = False,
                completed = True    
            )
   
        if decision == 2:
            player_picture = 'assets/portraits/portrait_test_1.jpeg'
            # enemie1 = Character("Capiroto", player_picture, 100, 15)
            # enemie2 = Character("demonio", player_picture, 100, 15)
            # enemie3 = Character("ditocujo", player_picture, 100, 15)

            # arena = Arena(self.screen, self.screen_rect, self.fps, self.resolution, allies, (enemie1, enemie2, enemie3))
            # arena.arena()

            return EventResponse(
                    back = False,
                    completed = True   
                )

        
        

