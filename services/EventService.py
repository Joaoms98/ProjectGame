import pygame
from objects.response import EventResponse

class EventService:
    def takeEvent(self):
        response = EventResponse("Ao chegar no local, voce se depera com uma estranha formacao aparentando ser um lago e em seu cento ha um pilar de pedra reluzindo um possivel artefato. Com uma boa pontaria e possivel jogar um gancho para pegar o item",
                                 "Interagir", "Sair")
        return response