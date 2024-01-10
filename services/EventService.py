from response.EventResponse import EventResponse

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
            return self.EventA1_2(decision, allies)

    def EventA1_1(self) -> EventResponse:
            return EventResponse(
                message="Ao chegar no local, voce se depera com uma estranha formacao aparentando"\
                    "ser um lago e em seu cento ha um pilar de pedra reluzindo um possivel"\
                    "artefato. Com uma boa pontaria e possivel jogar um gancho para pegar o item",
                decision1="Interagir",
                decision2="Sair",
                back = False        
            )

    def EventA1_2(self, decision: int, allies: list) -> EventResponse: 
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
                    back = True       
                )

